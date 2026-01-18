import io
import json
import random

from . import Data
from typing import TYPE_CHECKING, Optional
from BaseClasses import Item, Location
from settings import get_settings
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes, APPatchExtension
from .Items import item_table
from .Locations import shop, badge, pants, location_table, all_locations, specialCoins

if TYPE_CHECKING:
    from . import MLSSWorld

colors = [
    Data.redHat,
    Data.greenHat,
    Data.blueHat,
    Data.azureHat,
    Data.yellowHat,
    Data.orangeHat,
    Data.purpleHat,
    Data.pinkHat,
    Data.blackHat,
    Data.whiteHat,
    Data.silhouetteHat,
    Data.chaosHat,
    Data.truechaosHat
]

cpants = [
    Data.vanilla,
    Data.redPants,
    Data.greenPants,
    Data.bluePants,
    Data.azurePants,
    Data.yellowPants,
    Data.orangePants,
    Data.purplePants,
    Data.pinkPants,
    Data.blackPants,
    Data.whitePants,
    Data.chaosPants
]


def get_base_rom_as_bytes() -> bytes:
    with open(get_settings().mlss_options.rom_file, "rb") as infile:
        base_rom_bytes = bytes(infile.read())
    return base_rom_bytes


class MLSSPatchExtension(APPatchExtension):
    game = "Mario & Luigi Superstar Saga"

    @staticmethod
    def randomize_music(caller: APProcedurePatch, rom: bytes):
        options = json.loads(caller.get_file("options.json").decode("UTF-8"))
        if options["music_options"] in {0, 3}:
            return rom
        stream = io.BytesIO(rom)
        random.seed(options["seed"] + options["player"])

        songs = []
        removed_songs = [0x21CBD8, 0x21CBDC]

        if options["music_options"] == 1:
            removed_songs.extend([0x21CB74, 0x21CB78, 0x21CB88, 0x21CB8C, 0x21CC1C, 0x21CC24, 0x21CC28, 0x21CC2C])

        stream.seek(0x21CB74)
        for _ in range(50):
            if stream.tell() in removed_songs:
                stream.seek(4, 1)
                continue
            temp = stream.read(4)
            songs.append(temp)

        random.shuffle(songs)
        stream.seek(0x21CB74)
        for _ in range(50):
            if stream.tell() in removed_songs:
                stream.seek(4, 1)
                continue
            stream.write(songs.pop())

        return stream.getvalue()

    @staticmethod
    def hidden_visible(caller: APProcedurePatch, rom: bytes):
        options = json.loads(caller.get_file("options.json").decode("UTF-8"))
        if options["block_visibility"] == 0:
            return rom
        stream = io.BytesIO(rom)

        for location in [location for location in all_locations if location.itemType == 0]:
            stream.seek(location.id - 6)
            b = stream.read(1)
            if b[0] == 0x10 and options["block_visibility"] == 1:
                stream.seek(location.id - 6)
                stream.write(bytes([0x0]))
            if b[0] == 0x0 and options["block_visibility"] == 2:
                stream.seek(location.id - 6)
                stream.write(bytes([0x10]))

        return stream.getvalue()

    @staticmethod
    def randomize_sounds(caller: APProcedurePatch, rom: bytes):
        options = json.loads(caller.get_file("options.json").decode("UTF-8"))
        if options["randomize_sounds"] != 1:
            return rom
        stream = io.BytesIO(rom)
        random.seed(options["seed"] + options["player"])
        fresh_pointers = Data.sounds
        pointers = Data.sounds

        random.shuffle(pointers)
        stream.seek(0x21CC44, 0)
        for i in range(354):
            current_position = stream.tell()
            value = int.from_bytes(stream.read(3), "little")
            if value in fresh_pointers:
                stream.seek(current_position)
                stream.write(pointers.pop().to_bytes(3, "little"))
            stream.seek(1, 1)

        return stream.getvalue()

    @staticmethod
    def enemy_randomize(caller: APProcedurePatch, rom: bytes):
        options = json.loads(caller.get_file("options.json").decode("UTF-8"))
        if options["randomize_bosses"] == 0 and options["randomize_enemies"] == 0:
            return rom

        enemies = [pos for pos in Data.enemies if pos not in Data.bowsers] if options["castle_skip"] else Data.enemies
        bosses = [pos for pos in Data.bosses if pos not in Data.bowsers] if options["castle_skip"] else Data.bosses
        stream = io.BytesIO(rom)
        random.seed(options["seed"] + options["player"])

        if options["randomize_bosses"] == 1 or (options["randomize_bosses"] == 2 and options["randomize_enemies"] == 0):
            raw = []
            for pos in bosses:
                stream.seek(pos + 1)
                raw += [stream.read(0x1F)]
            random.shuffle(raw)
            for pos in bosses:
                stream.seek(pos + 1)
                stream.write(raw.pop())

        if options["randomize_enemies"] == 1:
            raw = []
            for pos in enemies:
                stream.seek(pos + 1)
                raw += [stream.read(0x1F)]
            if options["randomize_bosses"] == 2:
                for pos in bosses:
                    stream.seek(pos + 1)
                    raw += [stream.read(0x1F)]
            random.shuffle(raw)
            for pos in enemies:
                stream.seek(pos + 1)
                stream.write(raw.pop())
            if options["randomize_bosses"] == 2:
                for pos in bosses:
                    stream.seek(pos + 1)
                    stream.write(raw.pop())
            return stream.getvalue()

        enemies_raw = []
        groups = []
        boss_groups = []

        if options["randomize_enemies"] == 0:
            return stream.getvalue()

        if options["randomize_bosses"] == 2:
            for pos in bosses:
                stream.seek(pos + 1)
                boss_groups += [stream.read(0x1F)]

        for pos in enemies:
            stream.seek(pos + 8)
            for _ in range(6):
                enemy = int.from_bytes(stream.read(1), "little")
                if enemy > 0:
                    stream.seek(1, 1)
                    flag = int.from_bytes(stream.read(1), "little")
                    if flag == 0x7:
                        break
                    if flag in [0x0, 0x2, 0x4]:
                        if enemy not in Data.pestnut and enemy not in Data.flying:
                            enemies_raw += [enemy]
                    stream.seek(1, 1)
                else:
                    stream.seek(3, 1)

        random.shuffle(enemies_raw)
        chomp = False
        for pos in enemies:
            stream.seek(pos + 8)

            for _ in range(6):
                enemy = int.from_bytes(stream.read(1), "little")
                if enemy > 0 and enemy not in Data.flying and enemy not in Data.pestnut:
                    if enemy == 0x52:
                        chomp = True
                    stream.seek(1, 1)
                    flag = int.from_bytes(stream.read(1), "little")
                    if flag not in [0x0, 0x2, 0x4]:
                        stream.seek(1, 1)
                        continue
                    stream.seek(-3, 1)
                    stream.write(bytes([enemies_raw.pop()]))
                    stream.seek(1, 1)
                    stream.write(bytes([0x6]))
                    stream.seek(1, 1)
                else:
                    stream.seek(3, 1)

            stream.seek(pos + 1)
            raw = stream.read(0x1F)
            if chomp:
                raw = raw[0:3] + bytes([0x67, 0xAB, 0x28, 0x08]) + raw[7:]
            else:
                raw = raw[0:3] + bytes([0xEE, 0x2C, 0x28, 0x08]) + raw[7:]
            groups += [raw]
            chomp = False

        arr = enemies
        if options["randomize_bosses"] == 2:
            arr += bosses
            groups += boss_groups

        random.shuffle(groups)

        for pos in arr:
            if arr[-1] in boss_groups:
                stream.seek(pos)
                temp = stream.read(1)
                stream.seek(pos)
                stream.write(bytes([temp[0] | 0x80]))
            stream.seek(pos + 1)
            stream.write(groups.pop())

        return stream.getvalue()

    @staticmethod
    def randomize_backgrounds(caller: APProcedurePatch, rom: bytes):
        options = json.loads(caller.get_file("options.json").decode("UTF-8"))
        stream = io.BytesIO(rom)
        random.seed(options["seed"] + options["player"])

        all_enemies = list(range(0x50300C, 0x50300C + 0x1741, 0x20))
        for address in all_enemies:
            stream.seek(address + 8, 0)
            current_enemy = stream.read(1)
            stream.seek(address + 3, 0)

            if current_enemy in (0x9B, 0x9E): # Check for Roy and Morton (prevent unfair backgrounds)
                if options["randomize_backgrounds"]:
                    wavy_backgrounds = [0x02, 0x03, 0x05, 0x06, 0x0D, 0x22, 0x23, 0x24, 0x26]
                    stream.write(bytes([random.choice(wavy_backgrounds)]))
                elif current_enemy == 0x9B:
                    stream.write(bytes([0x24]))
                else:
                    stream.write(bytes([0x23]))
            elif current_enemy == 0x70: # Check for Wiggler (prevent unfair backgrounds)
                if options["randomize_backgrounds"]:
                    wavy_backgrounds = [0x01, 0x03, 0x05, 0x06, 0x07, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x20, 0x21, 0x23, 0x24, 0x25, 0x26, 0x27]
                    stream.write(bytes([random.choice(wavy_backgrounds)]))
                else:
                    stream.write(bytes([0x0F]))
            elif options["randomize_backgrounds"]:
                stream.write(bytes([random.randint(0, 0x27)]))

        return stream.getvalue()

    @staticmethod
    def randomize_bros_move_cost(caller: APProcedurePatch, rom: bytes):
        options = json.loads(caller.get_file("options.json").decode("UTF-8"))
        if options["randomize_bros_move_cost"] == 0: # Change setting: make it a choice, "none", "balanced", "fully_random"
            return rom
        stream = io.BytesIO(rom)
        random.seed(options["seed"] + options["player"])

        bp_list = Data.bros_values
        current_move = 0
        # 0: Splash Bros.       (4, 3)
        # 1: Swing Bros.        (6, 4)
        # 2: Chopper Bros.      (5, 3)
        # 3: Fire Bros.         (6, 3)
        # 4: Bounce Bros.       (4, 3)
        # 5: Knockback Bros.    (5, 3)
        # 6: Cyclone Bros.      (8, 4)
        # 7: Thunder Bros.      (6, 4)
        while current_move < len(bp_list):
            stream.seek(bp_list[current_move])
            if options["randomize_bros_move_cost"] == 3:
                new_move_value1 = random.randint(1, 15)
                new_move_value2 = random.randint(1, 15)
            elif current_move in {0, 1, 3, 4}: # Splash, Swing, Fire and Bounce have the lowest cost
                if options["randomize_bros_move_cost"] == 1:
                    new_move_value2 = random.randint(1, 6)
                    new_move_value1 = random.randint(new_move_value2 + 1, new_move_value2 + 3)
                elif options["randomize_bros_move_cost"] == 2:
                    new_move_value1 = random.randint(1, 6)
                    new_move_value2 = random.randint(new_move_value1 + 1, new_move_value1 + 3)

            elif current_move in {5, 7}: # Knockback Bros. and Thunder Bros. have medium cost
                if options["randomize_bros_move_cost"] == 1:
                    new_move_value2 = random.randint(2, 8)
                    new_move_value1 = random.randint(new_move_value2 + 1, new_move_value2 + 4)
                elif options["randomize_bros_move_cost"] == 2:
                    new_move_value1 = random.randint(2, 8)
                    new_move_value2 = random.randint(new_move_value1 + 1, new_move_value1 + 4)

            else: # Chopper Bros. and Cyclone Bros. have the highest cost
                if options["randomize_bros_move_cost"] == 1:
                    new_move_value2 = random.randint(4, 10)
                    new_move_value1 = random.randint(new_move_value2 + 2, new_move_value2 + 5)
                elif options["randomize_bros_move_cost"] == 2:
                    new_move_value1 = random.randint(4, 10)
                    new_move_value2 = random.randint(new_move_value1 + 2, new_move_value1 + 5)

            stream.write(bytes([new_move_value1, new_move_value2]))
            current_move += 1

        return stream.getvalue()

    @staticmethod
    def randomize_heal_item_value(caller: APProcedurePatch, rom: bytes):
        options = json.loads(caller.get_file("options.json").decode("UTF-8"))
        if options["randomize_heal_item_value"] == 0:
            return rom
        stream = io.BytesIO(rom)
        random.seed(options["seed"] + options["player"])

        item_list = Data.heal_values
        current_item = 0

        while current_item < len(item_list):
            if options["randomize_heal_item_value"] == 1:
                if current_item in {0, 3, 6}:
                    heal_value1 = random.randint(5, 50)
                    write_heal_value = heal_value1
                elif current_item in {1, 4, 7}:
                    heal_value2 = random.randint(heal_value1 + 10, heal_value1 + 55) # Max 100
                    write_heal_value = heal_value2
                else:
                    heal_value3 = random.randint(heal_value2 + 15, heal_value2 + 50) # Max 150
                    write_heal_value = heal_value3
            else:
                write_heal_value = random.randint(5, 150)

            stream.seek(item_list[current_item][0])
            stream.write(bytes([write_heal_value]))

            if current_item in {0, 1, 2}:
                mushroom_description = f"Recover {write_heal_value} HP."
                stream.seek(item_list[current_item][1] - 8)
                stream.write(mushroom_description.encode("ascii") + b'\x00')

            elif current_item in {3, 4, 5}:
                nut_description = f"Recover {write_heal_value} HP each."
                stream.seek(item_list[current_item][1] - 9)
                stream.write(nut_description.encode("ascii") + b'\x00')

                # Only required for Nut due to the lack of room after the description; moves the description backwards by one byte.
                # The following changes the offset to the new description location.
                stream.seek(item_list[current_item][2])
                new_offset = int.from_bytes(stream.read(1)) - 1
                stream.seek(-1, 1)
                stream.write(bytes([new_offset]))

            else:
                syrup_description = f"Recover {write_heal_value} Bros. points."
                stream.seek(item_list[current_item][1] - 8)
                stream.write(syrup_description.encode("ascii") + b'\x00')

            current_item += 1

        return stream.getvalue()

    @staticmethod
    def randomize_coffee_values(caller: APProcedurePatch, rom: bytes):
        options = json.loads(caller.get_file("options.json").decode("UTF-8"))
        if options["randomize_coffee_values"] == 0:
            return rom
        stream = io.BytesIO(rom)
        random.seed(options["seed"] + options["player"])

        coffee_list = Data.coffee_values
        current_coffee = 0
        temp_coffee_boolean = False

        while current_coffee < len(coffee_list):
            if options["randomize_coffee_values"] == 1:
                if not temp_coffee_boolean:
                    temp_coffee_boolean = True
                    coffee_value1 = random.randint(1, 15)
                    write_coffee_value = coffee_value1
                elif current_coffee == 6:
                    write_coffee_value = random.randint(coffee_value1 + 2, coffee_value1 + 7)
            else:
                write_coffee_value = random.randint(1, 15)

            stream.seek(coffee_list[current_coffee][0])
            stream.write(bytes([write_coffee_value]))

            match current_coffee:
                case 0:
                    coffee_description = f"Starbeans Blend: +{write_coffee_value} HP"
                    stream.seek(coffee_list[current_coffee][1] - 18)
                    stream.write(coffee_description.encode("ascii") + b'\x00')
                case 1:
                    coffee_description = f"Starbeans Blend: +{write_coffee_value} BP"
                    stream.seek(coffee_list[current_coffee][1] - 18)
                    stream.write(coffee_description.encode("ascii") + b'\x00')
                case 2:
                    coffee_description = f"Starbeans Blend: +{write_coffee_value} SPEED"
                    stream.seek(coffee_list[current_coffee][1] - 18)
                    stream.write(coffee_description.encode("ascii") + b'\x00')
                case 3:
                    coffee_description = f"Starbeans Blend: +{write_coffee_value} STACHE"
                    stream.seek(coffee_list[current_coffee][1] - 18)
                    stream.write(coffee_description.encode("ascii") + b'\x00')
                case 4:
                    coffee_description = f"Starbeans Blend: +{write_coffee_value} POW" # Same as Nut, needs to be moved backwards due to no space
                    stream.seek(coffee_list[current_coffee][1] - 19)
                    stream.write(coffee_description.encode("ascii") + b'\x00')

                    stream.seek(coffee_list[current_coffee][2])
                    new_offset = int.from_bytes(stream.read(1)) - 1
                    stream.seek(-1, 1)
                    stream.write(bytes([new_offset]))
                case 5:
                    coffee_description = f"Starbeans Blend: +{write_coffee_value} DEF" # This one needed an entirely new spot because there was not even one single free byte
                    stream.seek(0xD3F000)
                    stream.write(coffee_description.encode("ascii") + b'\x00')
                    stream.seek(coffee_list[current_coffee][2])
                    stream.write(bytes([0x00, 0xF0, 0xD3, 0x08]))
                case 6:
                    coffee_description = f"Starbeans Blend: +{write_coffee_value} ???"
                    stream.seek(coffee_list[current_coffee][1] - 19)
                    stream.write(coffee_description.encode("ascii") + b'\x00')

                    stream.seek(coffee_list[current_coffee][2])
                    new_offset = int.from_bytes(stream.read(1)) - 1
                    stream.seek(-1, 1)
                    stream.write(bytes([new_offset]))

            current_coffee += 1

        return stream.getvalue()

class MLSSProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Mario & Luigi Superstar Saga"
    hash = "4b1a5897d89d9e74ec7f630eefdfd435"
    patch_file_ending = ".apmlss"
    result_file_ending = ".gba"

    procedure = [
        ("apply_bsdiff4", ["base_patch.bsdiff4"]),
        ("apply_tokens", ["token_data.bin"]),
        ("enemy_randomize", []),
        ("hidden_visible", []),
        ("randomize_sounds", []),
        ("randomize_music", []),
        ("randomize_backgrounds", []),
        ("randomize_bros_move_cost", []),
        ("randomize_heal_item_value", []),
        ("randomize_coffee_values", []),
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_as_bytes()


def write_tokens(world: "MLSSWorld", patch: MLSSProcedurePatch) -> None:
    options_dict = {
        "randomize_enemies": world.options.randomize_enemies.value,
        "randomize_bosses": world.options.randomize_bosses.value,
        "randomize_backgrounds": world.options.randomize_backgrounds.value,
        "randomize_bros_move_cost": world.options.randomize_bros_move_cost.value,
        "randomize_heal_item_value": world.options.randomize_heal_item_value.value,
        "randomize_coffee_values": world.options.randomize_coffee_values.value,
        "castle_skip": world.options.castle_skip.value,
        "randomize_sounds": world.options.randomize_sounds.value,
        "music_options": world.options.music_options.value,
        "block_visibility": world.options.block_visibility.value,
        "seed": world.multiworld.seed,
        "player": world.player,
    }
    patch.write_file("options.json", json.dumps(options_dict).encode("UTF-8"))

    # Bake player name into ROM
    patch.write_token(APTokenTypes.WRITE, 0xDF0000, world.multiworld.player_name[world.player].encode("UTF-8"))

    # Bake seed name into ROM
    patch.write_token(APTokenTypes.WRITE, 0xDF00A0, world.multiworld.seed_name.encode("UTF-8"))

    # Intro Skip
    patch.write_token(
        APTokenTypes.WRITE,
        0x244D08,
        bytes([0x88, 0x0, 0x19, 0x91, 0x1, 0x20, 0x58, 0x1, 0xF, 0xA0, 0x3, 0x15, 0x27, 0x8]),
    )

    # Patch S.S Chuckola Loading Zones
    patch.write_token(APTokenTypes.WRITE, 0x25FD4E, bytes([0x48, 0x30, 0x80, 0x60, 0x50, 0x2, 0xF]))

    patch.write_token(APTokenTypes.WRITE, 0x25FD83, bytes([0x48, 0x30, 0x80, 0x60, 0xC0, 0x2, 0xF]))

    patch.write_token(APTokenTypes.WRITE, 0x25FDB8, bytes([0x48, 0x30, 0x05, 0x80, 0xE4, 0x0, 0xF]))

    patch.write_token(APTokenTypes.WRITE, 0x25FDED, bytes([0x48, 0x30, 0x06, 0x80, 0xE4, 0x0, 0xF]))

    patch.write_token(APTokenTypes.WRITE, 0x25FE22, bytes([0x48, 0x30, 0x07, 0x80, 0xE4, 0x0, 0xF]))

    patch.write_token(APTokenTypes.WRITE, 0x25FE57, bytes([0x48, 0x30, 0x08, 0x80, 0xE4, 0x0, 0xF]))

    patch.write_token(APTokenTypes.WRITE, 0x3A79C0, bytes([0x16])) #Add song to room 0x09

    if world.options.extra_pipes:
        patch.write_token(APTokenTypes.WRITE, 0xD00001, bytes([0x1]))

    if world.options.castle_skip:
        patch.write_token(APTokenTypes.WRITE, 0x3AEAB0, bytes([0xC1, 0x67, 0x0, 0x6, 0x1C, 0x08, 0x3]))
        patch.write_token(APTokenTypes.WRITE, 0x3AEC18, bytes([0x89, 0x65, 0x0, 0xE, 0xA, 0x08, 0x1]))
        patch.write_token(APTokenTypes.WRITE, 0xD00012, bytes([world.options.castle_skip.value]))

    if world.options.skip_minecart:
        patch.write_token(APTokenTypes.WRITE, 0x3AC728, bytes([0x89, 0x13, 0x0, 0x10, 0xF, 0x08, 0x1]))
        patch.write_token(APTokenTypes.WRITE, 0x3AC56C, bytes([0x49, 0x16, 0x0, 0x8, 0x8, 0x08, 0x1]))
        patch.write_token(APTokenTypes.WRITE, 0xD00013, bytes([world.options.skip_minecart.value]))

    if world.options.scale_stats:
        patch.write_token(APTokenTypes.WRITE, 0xD00002, bytes([0x1]))

    patch.write_token(APTokenTypes.WRITE, 0xD00003, bytes([world.options.xp_multiplier.value]))

    if world.options.goal == 1:
        patch.write_token(APTokenTypes.WRITE, 0xD00008, bytes([world.options.goal.value]))
        patch.write_token(APTokenTypes.WRITE, 0xD00009, bytes([world.options.emblems_required.value]))

    if world.options.tattle_hp:
        patch.write_token(APTokenTypes.WRITE, 0xD00000, bytes([0x1]))

    if world.options.music_options == 3:
        patch.write_token(APTokenTypes.WRITE, 0x19B118, bytes([0x0, 0x25]))

    if world.options.coins != 0:
        patch.write_token(APTokenTypes.WRITE, 0xD00010, bytes([world.options.coins.value]))

    if world.options.difficult_logic:
        patch.write_token(APTokenTypes.WRITE, 0xD00011, bytes([world.options.difficult_logic.value]))

    if world.options.disable_surf:
        patch.write_token(APTokenTypes.WRITE, 0xD00014, bytes([world.options.disable_surf.value]))

    if world.options.disable_harhalls_pants:
        patch.write_token(APTokenTypes.WRITE, 0xD00015, bytes([world.options.disable_harhalls_pants]))

    if world.options.chuckle_beans != 0:
        patch.write_token(APTokenTypes.WRITE, 0xD00016, bytes([world.options.chuckle_beans.value]))

    if world.options.red_goblet_required:
        patch.write_token(APTokenTypes.WRITE, 0xD00017, bytes([world.options.red_goblet_required.value]))

    if world.options.randomize_bosses != 0:
        patch.write_token(APTokenTypes.WRITE, 0xD00018, bytes([world.options.randomize_bosses.value]))

    for location_name in location_table.keys():
        if location_name in world.disabled_locations:
            continue
        location = world.get_location(location_name)
        item = location.item
        address = [address for address in all_locations if address.name == location.name]
        item_inject(world, patch, location.address, address[0].itemType, item)
        if "Shop" in location_name and "Coffee" not in location_name and item.player != world.player:
            desc_inject(world, patch, location, item)

    swap_colors(world, patch, world.options.mario_pants.value, 0, True)
    swap_colors(world, patch, world.options.luigi_pants.value, 1, True)
    swap_colors(world, patch, world.options.mario_color.value, 0)
    swap_colors(world, patch, world.options.luigi_color.value, 1)

    move_blocks(world, patch)

    patch.write_file("token_data.bin", patch.get_token_binary())

def move_blocks(world: "MLSSWorld", patch: MLSSProcedurePatch):
    trsr_data = []
    trsr_pointer = []
    trsr_count = 0
    trsr_total = 0
    curRoomID = 0

    while curRoomID < 512:
        for sublist in Data.treasureList:
            if sublist[0] == curRoomID:
                trsr_count += 1
                trsr_total += 1
        trsr_countMemory = trsr_count
        trsr_count = trsr_total - trsr_countMemory
        while trsr_count < trsr_total:
            for item in Data.treasureList[trsr_count][1:]:
                trsr_data.append(item.to_bytes())
            trsr_count += 1
        trsr_pointerCurrent = (len(b''.join(trsr_data)) + 0x08D40000).to_bytes(4, "little")
        trsr_pointer.append(trsr_pointerCurrent)
        trsr_count = 0
        trsr_data.append(trsr_countMemory.to_bytes())
        trsr_data.append((trsr_total - trsr_countMemory).to_bytes(2, "little"))
        if trsr_countMemory > 0:
            trsr_data.append((trsr_countMemory * 8).to_bytes(2, "little"))
        curRoomID += 1

    patch.write_token(APTokenTypes.WRITE,0xD40000, b''.join(trsr_data))
    patch.write_token(APTokenTypes.WRITE,0x51FA00, b''.join(trsr_pointer))

    if world.options.coins != 2:
        for location in [location for location in all_locations if location in specialCoins]:
            patch.write_token(APTokenTypes.WRITE, location.id - 5, bytes([0x70, 0x70]))
    else:
        for item in Data.deactivate_object_blocks[:]:
            patch.write_token(APTokenTypes.WRITE, item, bytes([0xE0]))

def swap_colors(world: "MLSSWorld", patch: MLSSProcedurePatch, color: int, bro: int,
                pants_option: Optional[bool] = False):
    if not pants_option and color == bro:
        return
    chaos = False
    if not pants_option and color == 11 or color == 12:
        chaos = True
    if pants_option and color == 11:
        chaos = True
    for c in [c for c in (cpants[color] if pants_option else colors[color])
              if (c[3] == bro if not chaos else c[1] == bro)]:
        if chaos:
            patch.write_token(APTokenTypes.WRITE, c[0],
                              bytes([world.random.randint(0, 255), world.random.randint(0, 127)]))
        else:
            patch.write_token(APTokenTypes.WRITE, c[0], bytes([c[1], c[2]]))


def item_inject(world: "MLSSWorld", patch: MLSSProcedurePatch, location: int, item_type: int, item: Item):
    if item.player == world.player:
        code = item_table[item.name].itemID
    else:
        code = 0x3F
    if item_type == 0:
        patch.write_token(APTokenTypes.WRITE, location, bytes([code]))
    elif item_type == 1:
        if code == 0x1D or code == 0x1E:
            code += 0xE
        if 0x20 <= code <= 0x26:
            code -= 0x4
        insert = int(code)
        insert2 = insert % 0x10
        insert2 *= 0x10
        insert //= 0x10
        insert += 0x20
        patch.write_token(APTokenTypes.WRITE, location, bytes([insert, insert2]))
    elif item_type == 2:
        if code == 0x1D or code == 0x1E:
            code += 0xE
        if 0x20 <= code <= 0x26:
            code -= 0x4
        patch.write_token(APTokenTypes.WRITE, location, bytes([code]))
    elif item_type == 3:
        if code == 0x1D or code == 0x1E:
            code += 0xE
        if code < 0x1D:
            code -= 0xA
        if 0x20 <= code <= 0x26:
            code -= 0xE
        patch.write_token(APTokenTypes.WRITE, location, bytes([code]))
    else:
        patch.write_token(APTokenTypes.WRITE, location, bytes([0x18]))


def desc_inject(world: "MLSSWorld", patch: MLSSProcedurePatch, location: Location, item: Item):
    index = -1
    for key, value in shop.items():
        if location.address in value:
            if key == 0x3C05F0:
                index = value.index(location.address)
            else:
                index = value.index(location.address) + 14

    for key, value in badge.items():
        if index != -1:
            break
        if location.address in value:
            if key == 0x3C0618:
                index = value.index(location.address) + 24
            else:
                index = value.index(location.address) + 41

    for key, value in pants.items():
        if index != -1:
            break
        if location.address in value:
            if key == 0x3C0618:
                index = value.index(location.address) + 48
            else:
                index = value.index(location.address) + 66

    dstring = f"{world.multiworld.player_name[item.player]}: {item.name}"
    patch.write_token(APTokenTypes.WRITE, 0xD12000 + (index * 0x40), dstring.encode("UTF8"))
