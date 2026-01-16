from Options import Choice, Toggle, StartInventoryPool, PerGameCommonOptions, Range, Removed, OptionGroup
from dataclasses import dataclass


class SkipBowsersCastle(Toggle):
    """
    Skip straight from the Entrance Hall to Bowletta in Bowser's Castle.
    All Bowser's Castle locations will be removed from the location pool.
    """

    display_name = "Skip Bowser's Castle"

class ExtraPipes(Toggle):
    """
    Gives the player access to pipes 1, 3, 4, and 6 from the start.
    """

    display_name = "Start With Extra Pipes"

class SkipMinecart(Toggle):
    """
    Skip the minecart minigame that leads you through Hoohoo Mountain Base.
    This will remove the 1 location in the minecart cave from the location pool.
    """

    display_name = "Skip Minecart Minigame"

class DisableSurf(Toggle):
    """
    Remove the surf minigame location from the location pool.
    """

    display_name = "Disable Surf Minigame"

class MusicOptions(Choice):
    """
    Choose if you want to randomize or disable music.

    Default: Music will be untouched.

    Randomize: Music will be randomized.

    Disable: All music will be disabled. No music will play throughout the entire game.
    """

    display_name = "Music Options"
    option_default = 0
    option_randomize = 1
    option_disable = 2
    default = 0

class RandomSounds(Toggle):
    """
    Randomizes every sound in the game, minus a select few that can softlock the game.
    """

    display_name = "Randomize Sounds"

class MarioColor(Choice):
    """
    This changes the color of Mario's hat, as well as some key colors that are red including UI etc.
    """

    display_name = "Mario's Color"
    option_red = 0
    option_green = 1
    option_blue = 2
    option_cyan = 3
    option_yellow = 4
    option_orange = 5
    option_purple = 6
    option_pink = 7
    option_black = 8
    option_white = 9
    option_silhouette = 10
    option_chaos = 11
    option_true_chaos = 12
    default = 0

class LuigiColor(Choice):
    """
    This changes the color of Luigi's hat, as well as some key colors that are green including UI etc.
    """

    display_name = "Luigi's Color"
    option_red = 0
    option_green = 1
    option_blue = 2
    option_cyan = 3
    option_yellow = 4
    option_orange = 5
    option_purple = 6
    option_pink = 7
    option_black = 8
    option_white = 9
    option_silhouette = 10
    option_chaos = 11
    option_true_chaos = 12
    default = 1

class MarioPants(Choice):
    """
    This changes the color of Mario's trousers.
    """

    display_name = "Mario's Pants Color"
    option_vanilla = 0
    option_red = 1
    option_green = 2
    option_blue = 3
    option_cyan = 4
    option_yellow = 5
    option_orange = 6
    option_purple = 7
    option_pink = 8
    option_black = 9
    option_white = 10
    option_chaos = 11
    default = 0

class LuigiPants(Choice):
    """
    This changes the color of Luigi's trousers.
    """

    display_name = "Luigi's Pants Color"
    option_vanilla = 0
    option_red = 1
    option_green = 2
    option_blue = 3
    option_cyan = 4
    option_yellow = 5
    option_orange = 6
    option_purple = 7
    option_pink = 8
    option_black = 9
    option_white = 10
    option_chaos = 11
    default = 0

class RandomizeEnemies(Choice):
    """
    Randomize all normal enemy encounters in the game.
    If Bowser's castle skip is enabled, then enemies from Bowser's Castle will not be included.

    Disabled: Enemies will not be randomized.

    Vanilla Groups: Vanilla enemy groups will be shuffled with each other. Custom enemy groups will not be made.

    Custom Groups: Custom enemy groups will be made and shuffled. Some enemy groups will only be semi-random,
    including groups with flying enemies or pestnuts in them.
    """

    display_name = "Randomize Enemies"
    option_disabled = 0
    option_vanilla_groups = 1
    option_custom_groups = 2
    default = 0

class RandomizeBosses(Choice):
    """
    Randomize all boss encounters in the game.
    If Bowser's castle skip is enabled then bosses from Bowser's Castle will not be included.
    Some bosses are not randomized due to flags, and story (such as the final boss).

    Disabled: Bosses will not be randomized.

    Boss Only: Bosses will only be swapped with another boss.

    Boss Normal: Bosses can be swapped with normal enemy encounters.
    """

    display_name = "Randomize Bosses"
    option_disabled = 0
    option_boss_only = 1
    option_boss_normal = 2
    default = 0

class ScaleStats(Toggle):
    """
    This scales enemy HP, POW, DEF, and XP to vanilla values.
    This setting is intended for use with the Enemy Randomizer and is recommended to turn on.
    If you are not using the Enemy Randomizer the effects will be minimal.
    """

    display_name = "Scale Enemy Stats"

class XPMultiplier(Range):
    """
    This will multiply any XP you receive in battle by the chosen multiplier.
    """

    display_name = "XP Multiplier"
    range_start = 0
    range_end = 4
    default = 1

class TattleHp(Toggle):
    """
    This will display the enemies' current and max health while in battle.
    """

    display_name = "Tattle HP"

class RandomizeBackgrounds(Toggle):
    """
    This randomizes the background image in battles.
    """

    display_name = "Randomize Battle Backgrounds"

class HiddenVisible(Choice):
    """
    This makes any hidden blocks in the game into regular item blocks and vice versa.

    Disabled: Hidden blocks will remain invisible.

    Hidden Visible: Hidden blocks will turn visible to the player.

    Blocks Invisible: All item blocks will turn invisible. Hidden blocks will also remain invisible.
    """

    display_name = "Item Block Visibility"
    option_disabled = 0
    option_hidden_visible = 1
    option_blocks_invisible = 2
    default = 0

class Coins(Choice):
    """
    Add coin blocks in the game to the location pool.

    None: No coin blocks are added.

    Regular: Only the regular coin blocks are added.

    All: All coin blocks are added. This replaces the special coin blocks and the prototype blocks from Woohoo Hooniversity with regular randomized blocks.
    """

    display_name = "Coin Blocks"
    option_none = 0
    option_regular = 1
    option_all = 2
    default = 0

class HarhallsPants(Toggle):
    """
    This will remove the Harhall's Pants check from the pool.
    """

    display_name = "Remove Harhall's Pants"

class DifficultLogic(Toggle):
    """
    This adjusts the logic to be more difficult in a few areas,
    allowing for the logic to account for players getting to certain areas in unintended ways.
    Enable at your own risk, this is not an option made for beginners.
    """

    display_name = "Difficult Logic"

class ChuckleBeans(Choice):
    """
    Choose how you want chuckle bean digspots to be randomized.
    An amount of chuckle beans will be removed from the item pool,
    equal to the amount of locations removed by the setting that you choose.

    None: No chuckle bean digspots will be added into the location pool.

    Only Visible: Only chuckle bean digspots clearly marked with an X will be added into the location pool.

    All: All chuckle bean digspots will be added into the location pool.
    """

    display_name = "Chuckle Beans"
    option_none = 0
    option_only_visible = 1
    option_all = 2
    default = 2

class RedGobletRequired(Toggle):
    """
    Choose whether hidden chuckle bean digspots, Bean Fruits and Beanstones logically require Red Goblet.
    Tip: Mini Mario can find hidden digspots with an exclamation mark above his head, making these hidden digspots easier to find.
    """
    display_name = "Red Goblet Required"

class Goal(Choice):
    """
    Vanilla: Complete jokes end with the required items and defeat Birdo to unlock Bowser's Castle.

    Emblem Hunt: Find the required number of Beanstar Emblems to gain access to Bowser's Castle.
    """
    display_name = "Goal"
    option_vanilla = 0
    option_emblem_hunt = 1
    default = 0

class EmblemsRequired(Range):
    """
    Number of Beanstar Emblems to collect to unlock Bowser's Castle.

    If Goal is not Emblem Hunt, this does nothing.
    """
    display_name = "Emblems Required"
    range_start = 1
    range_end = 100
    default = 50

class EmblemsAmount(Range):
    """
    Number of Beanstar Emblems that are in the pool.

    If Goal is not Emblem Hunt, this does nothing.
    """
    display_name = "Emblems Available"
    range_start = 1
    range_end = 150
    default = 75

class RandomizeBPCost(Choice):
    """
    Randomize how much BP Bros. Moves cost in battle.

    Vanilla: Does not randomize Bros. Move cost.

    Balanced: Modes 1 and 2 always cost more than Mode 3.

    Reverse Balanced: Mode 3 always cost more than Modes 1 and 2.

    Fully Random: It is fully random with zero balancing. Moves cost between 1 and 15 BP.

    For both Balanced and Reverse Balanced, stronger moves cost more BP on average.
    """
    display_name = "Randomize Bros. Move Cost"
    option_vanilla = 0
    option_balanced = 1
    option_reverse_balanced = 2
    option_fully_random = 3
    default = 0

class RandomizeHealItemValue(Choice):
    """
    Randomize how much items heal you.

    Vanilla: Does not randomize heal values.

    Progressive: Better items heal more.

    Fully Random: Heal values are fully random with zero balancing. Items heal between 5 and 150 HP/BP.
    """
    option_vanilla = 0
    option_progressive = 1
    option_fully_random = 2
    display_name = "Randomize Heal Item Values"

class RandomizeCoffeeValues(Choice):
    """
    Randomize how much coffee increase your stats.

    Vanilla: Does not randomize coffee values.

    Consistent: All coffee increase by the same value. Teeheespresso will give more than the other coffees.

    Fully Random: All coffee have completely random values.
    """
    display_name = "Randomize Coffee Values"
    option_vanilla = 0
    option_consistent = 1
    option_fully_random = 2
    default = 0

mlss_option_groups = [
    OptionGroup("Logic Options", [
        Goal,
        EmblemsRequired,
        EmblemsAmount,
        Coins,
        ChuckleBeans,
        RedGobletRequired,
        SkipMinecart,
        DisableSurf,
        HarhallsPants,
        SkipBowsersCastle,
        DifficultLogic,
    ]),
    OptionGroup("Enemy Randomization", [
        RandomizeEnemies,
        RandomizeBosses,
        ScaleStats,
        XPMultiplier,
        TattleHp,
    ]),
    OptionGroup("Extras", [
        ExtraPipes,
        HiddenVisible,
        RandomizeBackgrounds,
        RandomizeBPCost,
        RandomizeHealItemValue,
        RandomizeCoffeeValues,
        MusicOptions,
        RandomSounds,
        MarioColor,
        LuigiColor,
        MarioPants,
        LuigiPants,
    ])
]

@dataclass
class MLSSOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    coins: Coins
    difficult_logic: DifficultLogic
    castle_skip: SkipBowsersCastle
    extra_pipes: ExtraPipes
    skip_minecart: SkipMinecart
    disable_surf: DisableSurf
    disable_harhalls_pants: HarhallsPants
    harhalls_pants: Removed
    block_visibility: HiddenVisible
    chuckle_beans: ChuckleBeans
    red_goblet_required: RedGobletRequired
    goal: Goal
    emblems_required: EmblemsRequired
    emblems_amount: EmblemsAmount
    music_options: MusicOptions
    randomize_sounds: RandomSounds
    randomize_enemies: RandomizeEnemies
    randomize_bosses: RandomizeBosses
    randomize_backgrounds: RandomizeBackgrounds
    scale_stats: ScaleStats
    xp_multiplier: XPMultiplier
    randomize_bros_move_cost: RandomizeBPCost
    randomize_heal_item_value: RandomizeHealItemValue
    randomize_coffee_values: RandomizeCoffeeValues
    tattle_hp: TattleHp
    mario_color: MarioColor
    luigi_color: LuigiColor
    mario_pants: MarioPants
    luigi_pants: LuigiPants
