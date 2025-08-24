import typing

from BaseClasses import Location


class LocationData:
    def __init__(self, name, id_, special_id, itemType):
        self.name = name
        self.itemType = itemType
        self.id = id_
        self.special_id = special_id


class MLSSLocation(Location):
    game: str = "Mario & Luigi Superstar Saga"


hidden = [
    0x39D8C5,# 0xD402D5,
    0x39D90F,# 0xD40327,
    0x39D9E9,# 0xD4040B,
    0x39DB02,# 0xD40534,
    0x39DAB5,# 0xD404DF,
    0x39DB0F,# 0xD40549,
    0x39DB2A,# 0xD40564,
    0x39DB32,# 0xD4056C,
    0x39DBBC,# 0xD405F6,
    0x39DBE1,# 0xD4061B,
    0x39DC65,# 0xD4069F,
    0x39DC5D,# 0xD40697,
    0x39DC82,# 0xD406BC,
    0x39DCC4,# 0xD406FE,
    0x39DCE1,# 0xD4071B,
    0x39DD13,# 0xD4074D,
    0x39DDF6,# 0xD40838,
    0x39DEA8,# 0xD408F2,
    0x39DED7,# 0xD40921,
    0x39DF63,# 0xD409B5,
    0x39E077,# 0xD40AE5,
    0x39E092,# 0xD40B00,
    0x39E0CD,# 0xD40B3B,
    0x39E0FA,# 0xD40B68,
    0x39E102,# 0xD40B70,
    0x39E187,# 0xD40BF5,
    0x39E1BC,# 0xD40C2A,
    0x39E1C9,# 0xD40C3F,
    0x39E1E3,# 0xD40C59,
    0x39E21D,# 0xD40C9B,
    0x39E232,# 0xD40CB0,
    0x39E2DC,# 0xD40D76,
    0x39E2E9,# 0xD40D8B,
    0x39E316,# 0xD40DB8,
    0x39E343,# 0xD40DED,
    0x39E370,# 0xD40E1A,
    0x39E396,# 0xD40E4A,
    0x39E3D1,# 0xD40E97,
    0x39E3F3,# 0xD40EB9,
    0x39E462,# 0xD40F28,
    0x39E477,# 0xD40F3D,
    0x39E51E,# 0xD40FE4,
    0x39E5B5,# 0xD41083,
    0x39E5C8,# 0xD41096,
    0x39E5D0,# 0xD4109E,
    0x39E5F0,# 0xD410BE,
    0x39E5FD,# 0xD410CB,
    0x39E6C2,# 0xD4119A,
    0x39E6CF,# 0xD411A7,
    0x39E702,# 0xD411E2,
    0x39E857,# 0xD41351,
    0x39E8A3,# 0xD413B9,
    0x39E91A,# 0xD4143A,
    0x39E944,# 0xD41464,
    0x39E959,# 0xD41479,
    0x39E983,# 0xD414A3,
    0x39E9A0,# 0xD414C0,
    0x39EC40,# 0xD417BA,
    0x39EC4D,# 0xD417C7,
]


mainArea: typing.List[LocationData] = [
    LocationData("Stardust Fields Room 1 Block 1", 0x39D65D, 0xD40045, 0),
    LocationData("Stardust Fields Room 1 Block 2", 0x39D665, 0xD4004D, 0),
    LocationData("Stardust Fields Room 2 Block", 0x39D678, 0xD40060, 0),
    LocationData("Stardust Fields Room 3 Block", 0x39D6AD, 0xD4009D, 0),
    LocationData("Stardust Fields Room 4 Block 1", 0x39D6CA, 0xD400C2, 0),
    LocationData("Stardust Fields Room 4 Block 2", 0x39D6C2, 0xD400BA, 0),
    LocationData("Stardust Fields Room 4 Block 3", 0x39D6BA, 0xD400B2, 0),
    LocationData("Stardust Fields Room 5 Block", 0x39D713, 0xD40113, 0),
    LocationData("Hoohoo Village Hammer House Block", 0x39D731, 0xD40139, 0),
    LocationData("Hoohoo Mountain Below Summit Block 1", 0x39D873, 0xD40283, 0),
    LocationData("Hoohoo Mountain Below Summit Block 2", 0x39D87B, 0xD4028B, 0),
    LocationData("Hoohoo Mountain Below Summit Block 3", 0x39D883, 0xD40293, 0),
    LocationData("Hoohoo Mountain Past Hoohooros Block 1", 0x39D890, 0xD402A0, 0),
    LocationData("Hoohoo Mountain Past Hoohooros Block 2", 0x39D8A0, 0xD402B0, 0),
    LocationData("Hoohoo Mountain Hoohooros Room Block 1", 0x39D8AD, 0xD402BD, 0),
    LocationData("Hoohoo Mountain Hoohooros Room Block 2", 0x39D8B5, 0xD402C5, 0),
    LocationData("Hoohoo Mountain Before Hoohooros Block", 0x39D8D2, 0xD402E2, 0),
    LocationData("Hoohoo Mountain Fountain Room Block 1", 0x39D8F2, 0xD40302, 0),
    LocationData("Hoohoo Mountain Fountain Room Block 2", 0x39D8FA, 0xD4030A, 0),
    LocationData("Hoohoo Mountain Room 1 Block 1", 0x39D91C, 0xD40334, 0),
    LocationData("Hoohoo Mountain Room 1 Block 2", 0x39D924, 0xD4033C, 0),
    LocationData("Hoohoo Mountain Room 1 Block 3", 0x39D92C, 0xD40344, 0),
    LocationData("Hoohoo Mountain Base Room 1 Block", 0x39D939, 0xD40351, 0),
    LocationData("Hoohoo Village Eastside Block", 0x39D957, 0xD40379, 0),
    LocationData("Hoohoo Village Bridge Room Block 1", 0x39D96F, 0xD40391, 0),
    LocationData("Hoohoo Village Bridge Room Block 2", 0x39D97F, 0xD403A1, 0),
    LocationData("Hoohoo Village Bridge Room Block 3", 0x39D98F, 0xD403B1, 0),
    LocationData("Hoohoo Mountain Base Bridge Room Block 1", 0x39D99C, 0xD403BE, 0),
    LocationData("Hoohoo Mountain Base Bridge Room Block 2", 0x39D9A4, 0xD403C6, 0),
    LocationData("Hoohoo Mountain Base Bridge Room Block 3", 0x39D9AC, 0xD403CE, 0),
    LocationData("Hoohoo Mountain Base Bridge Room Block 4", 0x39D9B4, 0xD403D6, 0),
    LocationData("Hoohoo Mountain Base Bridge Room Digspot", 0x39D9BC, 0xD403DE, 0),
    LocationData("Hoohoo Mountain Base Boostatue Room Block 1", 0x39D9C9, 0xD403EB, 0),
    LocationData("Hoohoo Mountain Base Boostatue Room Block 2", 0x39D9D1, 0xD403F3, 0),
    LocationData("Hoohoo Mountain Base Boostatue Room Digspot 1", 0x39D9D9, 0xD403FB, 0),
    LocationData("Hoohoo Mountain Base Boostatue Room Digspot 2", 0x39D9E1, 0xD40403, 0),
    LocationData("Hoohoo Mountain Base Grassy Area Block 1", 0x39D9FE, 0xD40420, 0),
    LocationData("Hoohoo Mountain Base Grassy Area Block 2", 0x39D9F6, 0xD40418, 0),
    LocationData("Hoohoo Mountain Base Past Minecart Minigame Block 1", 0x39DA35, 0xD4045F, 0),
    LocationData("Hoohoo Mountain Base Past Minecart Minigame Block 2", 0x39DA2D, 0xD40457, 0),
    LocationData("Cave Connecting Stardust Fields and Hoohoo Village Block 1", 0x39DA77, 0xD404A1, 0),
    LocationData("Cave Connecting Stardust Fields and Hoohoo Village Block 2", 0x39DA7F, 0xD404A9, 0),
    LocationData("Hoohoo Village South Cave Block", 0x39DACD, 0xD404FF, 0),
    LocationData("Hoohoo Village North Cave Room 1 Block", 0x39DA98, 0xD404C2, 0),
    LocationData("Hoohoo Village North Cave Room 2 Block", 0x39DAAD, 0xD404D7, 0),
    LocationData("Beanbean Outskirts Surf Beach Block", 0x39DD03, 0xD4073D, 0),
    LocationData("Woohoo Hooniversity Star Room Block 1", 0x39E13D, 0xD40BAB, 0),
    LocationData("Woohoo Hooniversity Star Room Block 2", 0x39E145, 0xD40BB3, 0),
    LocationData("Woohoo Hooniversity Star Room Block 3", 0x39E14D, 0xD40BBB, 0),
    LocationData("Woohoo Hooniversity Sun Door Block 1", 0x39E15A, 0xD40BC8, 0),
    LocationData("Woohoo Hooniversity Sun Door Block 2", 0x39E162, 0xD40BD0, 0),
    LocationData("Woohoo Hooniversity West of Star Room 4 Block 1", 0x39E1F0, 0xD40C66, 0),
    LocationData("Woohoo Hooniversity West of Star Room 4 Block 2", 0x39E1F8, 0xD40C6E, 0),
    LocationData("Woohoo Hooniversity West of Star Room 4 Block 3", 0x39E200, 0xD40C76, 0),
    LocationData("Hoohoo Mountain Fountain Room 2 Block", 0x39E8F5, 0xD41415, 0),
    LocationData("Hoohoo Mountain Past Hoohooros Connector Room Block", 0x39E912, 0xD41432, 0),
    LocationData("Outside Woohoo Hooniversity Block", 0x39E9B5, 0xD414D5, 0),
    LocationData("Shop Starting Flag 1", 0x3C05F0, 0, 3),
    LocationData("Shop Starting Flag 2", 0x3C05F2, 0, 3),
    LocationData("Shop Starting Flag 3", 0x3C05F4, 0, 3),
    LocationData("Hoohoo Mountain Summit Digspot", 0x39D85E, 0xD4026E, 0),
    LocationData("Hoohoo Mountain Below Summit Digspot", 0x39D86B, 0xD4027B, 0),
    LocationData("Hoohoo Mountain Past Hoohooros Digspot", 0x39D898, 0xD402A8, 0),
    LocationData("Hoohoo Mountain Hoohooros Room Digspot 1", 0x39D8BD, 0xD402CD, 0),
    LocationData("Hoohoo Mountain Hoohooros Room Digspot 2", 0x39D8C5, 0xD402D5, 0),
    LocationData("Hoohoo Mountain Before Hoohooros Digspot", 0x39D8E2, 0xD402F2, 0),
    LocationData("Hoohoo Mountain Room 2 Digspot 1", 0x39D907, 0xD4031F, 0),
    LocationData("Hoohoo Mountain Room 2 Digspot 2", 0x39D90F, 0xD40327, 0),
    LocationData("Hoohoo Mountain Base Room 1 Digspot", 0x39D941, 0xD40359, 0),
    LocationData("Hoohoo Village Eastside Digspot", 0x39D95F, 0xD40381, 0),
    LocationData("Hoohoo Village Super Hammer Cave Digspot", 0x39DB02, 0xD40534, 0),
    LocationData("Hoohoo Village Super Hammer Cave Block", 0x39DAEA, 0xD4051C, 0),
    LocationData("Hoohoo Village North Cave Room 2 Digspot", 0x39DAB5, 0xD404DF, 0),
    LocationData("Hoohoo Mountain Base Minecart Cave Digspot", 0x39DB0F, 0xD40549, 0),
    LocationData("Beanbean Outskirts Farm Room Digspot 1", 0x39DB22, 0xD4055C, 0),
    LocationData("Beanbean Outskirts Farm Room Digspot 2", 0x39DB2A, 0xD40564, 0),
    LocationData("Beanbean Outskirts Farm Room Digspot 3", 0x39DB32, 0xD4056C, 0),
    LocationData("Beanbean Outskirts NW Block", 0x39DB87, 0xD405C1, 0),
    LocationData("Beanbean Outskirts NW Digspot", 0x39DB97, 0xD405D1, 0),
    LocationData("Beanbean Outskirts W Digspot 1", 0x39DBAC, 0xD405E6, 0),
    LocationData("Beanbean Outskirts W Digspot 2", 0x39DBB4, 0xD405EE, 0),
    LocationData("Beanbean Outskirts W Digspot 3", 0x39DBBC, 0xD405F6, 0),
    LocationData("Beanbean Outskirts SW Digspot 1", 0x39DBC9, 0xD40603, 0),
    LocationData("Beanbean Outskirts SW Digspot 2", 0x39DBD9, 0xD40613, 0),
    LocationData("Beanbean Outskirts SW Digspot 3", 0x39DBE1, 0xD4061B, 0),
    LocationData("Beanbean Outskirts N Room 1 Digspot", 0x39DBEE, 0xD40628, 0),
    LocationData("Beanbean Outskirts N Room 2 Digspot", 0x39DBFB, 0xD40635, 0),
    LocationData("Beanbean Outskirts S Room 1 Digspot 1", 0x39DC08, 0xD40642, 0),
    LocationData("Beanbean Outskirts S Room 1 Block", 0x39DC20, 0xD4065A, 0),
    LocationData("Beanbean Outskirts S Room 1 Digspot 2", 0x39DC28, 0xD40662, 0),
    LocationData("Beanbean Outskirts S Room 2 Block 1", 0x39DC4D, 0xD40687, 0),
    LocationData("Beanbean Outskirts NE Digspot 1", 0x39DC7A, 0xD406B4, 0),
    LocationData("Beanbean Outskirts NE Digspot 2", 0x39DC82, 0xD406BC, 0),
    LocationData("Beanbean Outskirts E Digspot 1", 0x39DC8F, 0xD406C9, 0),
    LocationData("Beanbean Outskirts E Digspot 2", 0x39DC97, 0xD406D1, 0),
    LocationData("Beanbean Outskirts E Digspot 3", 0x39DC9F, 0xD406D9, 0),
    LocationData("Beanbean Outskirts SE Digspot 1", 0x39DCAC, 0xD406E6, 0),
    LocationData("Beanbean Outskirts SE Digspot 2", 0x39DCBC, 0xD406F6, 0),
    LocationData("Beanbean Outskirts SE Digspot 3", 0x39DCC4, 0xD406FE, 0),
    LocationData("Beanbean Outskirts North Beach Digspot 1", 0x39DCD1, 0xD4070B, 0),
    LocationData("Beanbean Outskirts North Beach Digspot 2", 0x39DCE1, 0xD4071B, 0),
    LocationData("Beanbean Outskirts North Beach Digspot 3", 0x39DCD9, 0xD40713, 0),
    LocationData("Beanbean Outskirts South Beach Digspot", 0x39DCEE, 0xD40728, 0),
    LocationData("Woohoo Hooniversity West of Star Room Digspot 1", 0x39E17F, 0xD40BED, 0),
    LocationData("Woohoo Hooniversity West of Star Room Digspot 2", 0x39E187, 0xD40BF5, 0),
    LocationData("Woohoo Hooniversity West of Star Room 2 Digspot", 0x39E1D6, 0xD40C4C, 0),
    LocationData("Woohoo Hooniversity West of Star Room 3 Digspot", 0x39E1E3, 0xD40C59, 0),
    LocationData("Woohoo Hooniversity West of Star Room 4 Digspot 1", 0x39E208, 0xD40C7E, 0),
    LocationData("Woohoo Hooniversity West of Star Room 4 Digspot 2", 0x39E210, 0xD40C86, 0),
    LocationData("Woohoo Hooniversity West of Star Room 5 Digspot", 0x39E21D, 0xD40C9B, 0),
    LocationData("Woohoo Hooniversity Entrance to Mini Mario Room Digspot 1", 0x39E22A, 0xD40CA8, 0),
    LocationData("Woohoo Hooniversity Entrance to Mini Mario Room Digspot 2", 0x39E232, 0xD40CB0, 0),
    LocationData("Woohoo Hooniversity Entrance to Mini Mario Room 2 Digspot", 0x39E23F, 0xD40CBD, 0),
    LocationData("Woohoo Hooniversity Mini Mario Puzzle Block", 0x39E24C, 0xD40CD2, 0),
    LocationData("Woohoo Hooniversity Mini Mario Puzzle Digspot", 0x39E254, 0xD40CDA, 0),
    LocationData("Woohoo Hooniversity Mini Mario Puzzle Secret Area Block 1", 0x39E261, 0xD40CE7, 0),
    LocationData("Woohoo Hooniversity Mini Mario Puzzle Secret Area Block 2", 0x39E269, 0xD40CEF, 0),
    LocationData("Woohoo Hooniversity Mini Mario Puzzle Secret Area Block 3", 0x39E271, 0xD40CF7, 0),
    LocationData("Woohoo Hooniversity Mini Mario Puzzle Secret Area Block 4", 0x39E279, 0xD40CFF, 0),
    LocationData("Hoohoo Mountain Fountain Room 2 Digspot", 0x39E8FD, 0xD4141D, 0),
    LocationData("Hoohoo Mountain Past Hoohooros Connector Room Digspot 1", 0x39E90A, 0xD4142A, 0),
    LocationData("Hoohoo Mountain Past Hoohooros Connector Room Digspot 2", 0x39E91A, 0xD4143A, 0),
    LocationData("Beanbean Outskirts Secret Scroll 1", 0x1E9411, 0, 2),
    LocationData("Beanbean Outskirts Secret Scroll 2", 0x1E9412, 0, 2),
    LocationData("Beanbean Outskirts Bean Fruit 1", 0x229345, 0, 1),
    LocationData("Beanbean Outskirts Bean Fruit 2", 0x22954D, 0, 1),
    LocationData("Beanbean Outskirts Bean Fruit 3", 0x228A17, 0, 1),
    LocationData("Beanbean Outskirts Bean Fruit 4", 0x22913A, 0, 1),
    LocationData("Beanbean Outskirts Bean Fruit 5", 0x22890E, 0, 1),
    LocationData("Beanbean Outskirts Bean Fruit 6", 0x228775, 0, 1),
    LocationData("Beanbean Outskirts Bean Fruit 7", 0x1E9431, 0, 2),
    LocationData("Hoohoo Village Mole Behind Turtle", 0x277AB2, 0, 1),
    LocationData("Beanbean Outskirts Thunderhand Mole", 0x2779C8, 0, 1),
    LocationData("Hoohoo Mountain Peasley's Rose", 0x1E9430, 0, 2),
    LocationData("Beanbean Outskirts Super Hammer Upgrade", 0x1E9404, 0, 2),
    LocationData("Beanbean Outskirts Ultra Hammer Upgrade", 0x1E9405, 0, 2),
    LocationData("Beanbean Outskirts NE Solo Mario Mole 1", 0x1E9435, 0, 2),
    LocationData("Beanbean Outskirts NE Solo Mario Mole 2", 0x1E9436, 0, 2),
    LocationData("Hoohoo Village Hammers", 0x1E9403, 0, 2),
    LocationData("Beanbean Outskirts Solo Luigi Cave Mole", 0x242888, 0, 1),
    LocationData("Beanbean Outskirts Farm Room Mole Reward 1", 0x243844, 0, 1),
    LocationData("Beanbean Outskirts Farm Room Mole Reward 2", 0x24387D, 0, 1),
    LocationData("Beanbean Outskirts South of Hooniversity Guards Digspot 1", 0x39E990, 0xD414B0, 0),
    LocationData("Beanbean Outskirts South of Hooniversity Guards Digspot 2", 0x39E998, 0xD414B8, 0),
    LocationData("Beanbean Outskirts South of Hooniversity Guards Digspot 3", 0x39E9A0, 0xD414C0, 0),
    LocationData("Beanbean Outskirts Entrance to Hoohoo Mountain Base Digspot 1", 0x39EB5A, 0xD41696, 0),
    LocationData("Beanbean Outskirts Entrance to Hoohoo Mountain Base Digspot 2", 0x39EB62, 0xD4169E, 0),
    LocationData("Beanbean Outskirts Pipe 2 Room Digspot", 0x39EC40, 0xD417BA, 0),
    LocationData("Beanbean Outskirts Pipe 4 Room Digspot", 0x39EC4D, 0xD417C7, 0),
    LocationData("Beanbean Castle Town Mini Mario Block 1", 0x39D813, 0xD4021B, 0),
    LocationData("Beanbean Castle Town Mini Mario Block 2", 0x39D81B, 0xD40223, 0),
    LocationData("Beanbean Castle Town Mini Mario Block 3", 0x39D823, 0xD4022B, 0),
    LocationData("Beanbean Castle Town Mini Mario Block 4", 0x39D82B, 0xD40233, 0),
    LocationData("Beanbean Castle Town Mini Mario Block 5", 0x39D833, 0xD4023B, 0),
]

coins: typing.List[LocationData] = [
    LocationData("Stardust Fields Room 2 Coin Block 1", 0x39D680, 0xD40068, 0),
    LocationData("Stardust Fields Room 2 Coin Block 2", 0x39D688, 0xD40070, 0),
    LocationData("Stardust Fields Room 2 Coin Block 3", 0x39D690, 0xD40078, 0),
    LocationData("Stardust Fields Room 3 Coin Block 1", 0x39D69D, 0xD4008D, 0),
    LocationData("Stardust Fields Room 3 Coin Block 2", 0x39D6A5, 0xD40095, 0),
    LocationData("Stardust Fields Room 5 Coin Block 1", 0x39D6D7, 0xD400CF, 0),
    LocationData("Stardust Fields Room 5 Coin Block 2", 0x39D6DF, 0xD400D7, 0),
    LocationData("Stardust Fields Room 7 Coin Block 1", 0x39D70B, 0xD4010B, 0),
    LocationData("Stardust Fields Room 7 Coin Block 2", 0x39D71B, 0xD4011B, 0),
    LocationData("Beanbean Castle Town Passport Photo Room Coin Block", 0x39D803, 0xD4020B, 0),
    LocationData("Hoohoo Mountain Before Hoohooros Coin Block", 0x39D8DA, 0xD402EA, 0),
    LocationData("Hoohoo Village Bridge Room Coin Block 1", 0x39D977, 0xD40399, 0),
    LocationData("Hoohoo Village Bridge Room Coin Block 2", 0x39D987, 0xD403A9, 0),
    LocationData("Hoohoo Village North Cave Room 1 Coin Block", 0x39DAA0, 0xD404CA, 0),
    LocationData("Hoohoo Village South Cave Coin Block 1", 0x39DAC5, 0xD404F7, 0),
    LocationData("Hoohoo Village South Cave Coin Block 2", 0x39DAD5, 0xD40507, 0),
    LocationData("Hoohoo Mountain Base Boostatue Cave Coin Block 1", 0x39DAE2, 0xD40514, 0),
    LocationData("Hoohoo Mountain Base Boostatue Cave Coin Block 2", 0x39DAF2, 0xD40524, 0),
    LocationData("Hoohoo Mountain Base Boostatue Cave Coin Block 3", 0x39DAFA, 0xD4052C, 0),
    LocationData("Beanbean Outskirts NW Coin Block", 0x39DB8F, 0xD405C9, 0),
    LocationData("Beanbean Outskirts S Room 1 Coin Block", 0x39DC18, 0xD40652, 0),
    LocationData("Beanbean Outskirts S Room 2 Coin Block", 0x39DC3D, 0xD40677, 0),
    LocationData("Chateau Popple Room Coin Block 1", 0x39DD30, 0xD4076A, 0),
    LocationData("Chateau Popple Room Coin Block 2", 0x39DD40, 0xD4077A, 0),
    LocationData("Chucklehuck Woods Cave Room 1 Coin Block", 0x39DD7A, 0xD407BC, 0),
    LocationData("Chucklehuck Woods Cave Room 2 Coin Block", 0x39DD97, 0xD407D9, 0),
    LocationData("Chucklehuck Woods Cave Room 3 Coin Block", 0x39DDB4, 0xD407F6, 0),
    LocationData("Chucklehuck Woods Solo Luigi Cave Room 1 Coin Block 1", 0x39DB48, 0xD40582, 0),
    LocationData("Chucklehuck Woods Solo Luigi Cave Room 1 Coin Block 2", 0x39DB50, 0xD4058A, 0),
    LocationData("Chucklehuck Woods Pipe 5 Room Coin Block", 0x39DDE6, 0xD40828, 0),
    LocationData("Chucklehuck Woods Room 7 Coin Block", 0x39DE31, 0xD40873, 0),
    LocationData("Chucklehuck Woods Past Chuckleroot Coin Block", 0x39DF14, 0xD4095E, 0),
    LocationData("Chucklehuck Woods Koopa Room Coin Block", 0x39DF53, 0xD409A5, 0),
    LocationData("Chucklehuck Woods Winkle Area Cave Coin Block", 0x39DF80, 0xD409D2, 0),
    LocationData("Sewers Prison Room Coin Block", 0x39E01E, 0xD40A8C, 0),
    LocationData("Gwarhar Lagoon First Underwater Area Room 2 Coin Block", 0x39E455, 0xD40F1B, 0),
    LocationData("Teehee Valley Past Ultra Hammer Rocks Coin Block", 0x39E588, 0xD41056, 0),
    LocationData("S.S. Chuckola Storage Room Coin Block 1", 0x39E618, 0xD410E6, 0),
    LocationData("S.S. Chuckola Storage Room Coin Block 2", 0x39E620, 0xD410EE, 0),
    LocationData("Joke's End Second Floor West Room Coin Block", 0x39E771, 0xD41261, 0),
    LocationData("Joke's End North of Bridge Room Coin Block", 0x39E836, 0xD41326, 0),
    LocationData("Outside Woohoo Hooniversity Coin Block 1", 0x39E9AD, 0xD414CD, 0),
    LocationData("Outside Woohoo Hooniversity Coin Block 2", 0x39E9BD, 0xD414DD, 0),
    LocationData("Outside Woohoo Hooniversity Coin Block 3", 0x39E9C5, 0xD414E5, 0),
]

specialCoins: typing.List[LocationData] = [
    LocationData("Stardust Fields Room 2 Coin Block 4", 1, 0xD40080, 0),
    LocationData("Stardust Fields Room 3 Coin Block 3", 1, 0xD400A5, 0),
    LocationData("Stardust Fields Room 5 Coin Block 3", 1, 0xD400DF, 0),
    LocationData("Stardust Fields Room 7 Coin Block 3", 1, 0xD40123, 0),
    LocationData("Beanbean Castle Coin Block", 1, 0xD40243, 0),
    LocationData("Hoohoo Mountain Fountain Room Coin Block", 1, 0xD40312, 0),
    LocationData("Hoohoo Mountain Base East of Bridge Room Coin Block", 1, 0xD40366, 0),
    LocationData("Hoohoo Mountain Base Grassy Area Coin Block", 1, 0xD40428, 0),
    LocationData("Hoohoo Village North Cave Room 2 Coin Block", 1, 0xD404E7, 0),
    LocationData("Hoohoo Mountain Base Boostatue Cave Coin Block 4", 1, 0xD4053C, 0),
    LocationData("Chateau Barrel Room Coin Block", 1, 0xD4079F, 0),
    LocationData("Chucklehuck Woods Room 7 Coin Block 2", 1, 0xD40893, 0),
    LocationData("Winkle Area Coin Block", 1, 0xD40980, 0),
    LocationData("Chucklehuck Woods Winkle Area Cave Coin Block 2", 1, 0xD409DA, 0),
    LocationData("Oho Oasis Outside Fire Palace Coin Block", 1, 0xD409F6, 0),
    LocationData("Oho Oasis Thunder Palace Coin Block", 1, 0xD40A38, 0),
    LocationData("Woohoo Hooniversity Barrel Puzzle Entrance Coin Block", 1, 0xD40C32, 0),
    LocationData("Woohoo Hooniversity West of Star Room 4 Coin Block", 1, 0xD40C8E, 0),
    LocationData("Woohoo Hooniversity Entrance to Mini Mario Room 2 Coin Block", 1, 0xD40CC5, 0),
    LocationData("Woohoo Hooniversity Past Cackletta Room 2 Coin Block", 1, 0xD40D3F, 0),
    LocationData("Woohoo Hooniversity Past Cackletta Room 3 Coin Block", 1, 0xD40D4C, 0),
    LocationData("Airport Entrance Coin Block", 1, 0xD40D7E, 0),
    LocationData("Airport Eastside Coin Block", 1, 0xD40DC0, 0),
    LocationData("Gwarhar Lagoon Pipe to Oho Ocean Room Coin Block", 1, 0xD40E37, 0),
    LocationData("Gwarhar Lagoon Massage Parlor Entrance Coin Block", 1, 0xD40E52, 0),
    LocationData("Gwarhar Lagoon Stone Bridge Room Coin Block", 1, 0xD40E72, 0),
    LocationData("Teehee Valley Room 2 Coin Block", 1, 0xD41019, 0),
    LocationData("S.S. Chuckola East of Entrance Coin Block", 1, 0xD4110C, 0),
    LocationData("Joke's End West of First Boiler Room Coin Block", 1, 0xD411CD, 0),
    LocationData("Joke's End Northeast of Boiler Room 3 Coin Block", 1, 0xD41227, 0),
    LocationData("Joke's End Northeast of Boiler Room 2 Coin Block", 1, 0xD41244, 0),
    LocationData("Joke's End Furnace Room 2 Coin Block", 1, 0xD41339, 0),
    LocationData("Joke's End North of Second Boiler Room Coin Block", 1, 0xD4136E, 0),
    LocationData("Fungitown Embassy Building Room 1 Coin Block", 1, 0xD41399, 0),
    LocationData("Fungitown Embassy Building Room 2 Coin Block", 1, 0xD413A6, 0),
    LocationData("Fungitown Psycho Kamek House Coin Block", 1, 0xD413C9, 0),
    LocationData("Bowser's Castle Lemmy Room 1 Coin Block", 1, 0xD415CC, 0),
    LocationData("Bowser's Castle Roy Room 1 Coin Block", 1, 0xD415FB, 0),
    LocationData("Bowser's Castle Roy Room 4 Coin Block", 1, 0xD41632, 0),
    LocationData("Woohoo Hooniversity Prototype Room 1 Block", 1, 0xD4172F, 0),
    LocationData("Woohoo Hooniversity Prototype Room 2 Block 1", 1, 0xD4173C, 0),
    LocationData("Woohoo Hooniversity Prototype Room 2 Block 2", 1, 0xD41744, 0),
    LocationData("Woohoo Hooniversity Prototype Room 2 Block 3", 1, 0xD4174C, 0),
    LocationData("Woohoo Hooniversity Prototype Room 2 Block 4", 1, 0xD41754, 0),
    LocationData("Woohoo Hooniversity Prototype Room 3 Block 1", 1, 0xD41761, 0),
    LocationData("Woohoo Hooniversity Prototype Room 3 Block 2", 1, 0xD41769, 0),
]

baseUltraRocks: typing.List[LocationData] = [
    LocationData("Hoohoo Mountain Base Past Ultra Hammer Rocks Block 1", 0x39DA42, 0xD4046C, 0),
    LocationData("Hoohoo Mountain Base Past Ultra Hammer Rocks Block 2", 0x39DA4A, 0xD40474, 0),
    LocationData("Hoohoo Mountain Base Past Ultra Hammer Rocks Block 3", 0x39DA52, 0xD4047C, 0),
    LocationData("Hoohoo Mountain Base Boostatue Room Digspot 3 (Right Side)", 0x39D9E9, 0xD4040B, 0),
    LocationData("Hoohoo Mountain Base Mole Near Teehee Valley", 0x277A45, 0, 1),
    LocationData("Teehee Valley Entrance To Hoohoo Mountain Digspot", 0x39E5B5, 0xD41083, 0),
    LocationData("Teehee Valley Upper Maze Room 1 Block", 0x39E5E0, 0xD410AE, 0),
    LocationData("Teehee Valley Upper Maze Room 2 Digspot 1", 0x39E5C8, 0xD41096, 0),
    LocationData("Teehee Valley Upper Maze Room 2 Digspot 2", 0x39E5D0, 0xD4109E, 0),
    LocationData("Guffawha Ruins Block", 0x39E6A3, 0xD4117B, 0),
    LocationData("Hoohoo Mountain Base Guffawha Ruins Entrance Digspot", 0x39DA0B, 0xD40435, 0),
    LocationData("Hoohoo Mountain Base Teehee Valley Entrance Digspot", 0x39DA20, 0xD4044A, 0),
    LocationData("Hoohoo Mountain Base Teehee Valley Entrance Block", 0x39DA18, 0xD40442, 0),
]

booStatue: typing.List[LocationData] = [
    LocationData("Beanbean Outskirts Before Harhall Digspot 1", 0x39E951, 0xD41471, 0),
    LocationData("Beanbean Outskirts Before Harhall Digspot 2", 0x39E959, 0xD41479, 0),
    LocationData("Beanstar Piece Harhall", 0x1E9441, 0, 2),
    LocationData("Beanbean Outskirts Boostatue Mole", 0x1E9434, 0, 2),
    LocationData("Harhall's Pants", 0x1E9444, 0, 2),
    LocationData("Beanbean Outskirts S Room 2 Digspot 1", 0x39DC65, 0xD4069F, 0),
    LocationData("Beanbean Outskirts S Room 2 Digspot 2", 0x39DC5D, 0xD40697, 0),
    LocationData("Beanbean Outskirts S Room 2 Block 2", 0x39DC45, 0xD4067F, 0),
    LocationData("Beanbean Outskirts S Room 2 Digspot 3", 0x39DC35, 0xD4066F, 0),
]

chucklehuck: typing.List[LocationData] = [
    LocationData("Chateau Room 1 Digspot", 0x39DD20, 0xD4075A, 0),
    LocationData("Chateau Popple Fight Room Block 1", 0x39DD38, 0xD40772, 0),
    LocationData("Chateau Popple Fight Room Block 2", 0x39DD48, 0xD40782, 0),
    LocationData("Chateau Popple Fight Room Digspot", 0x39DD50, 0xD4078A, 0),
    LocationData("Chateau Barrel Room Digspot", 0x39DD5D, 0xD40797, 0),
    LocationData("Chateau Goblet Room Digspot", 0x39DD6D, 0xD407AF, 0),
    LocationData("Chucklehuck Woods Cave Room 1 Block 1", 0x39DD82, 0xD407C4, 0),
    LocationData("Chucklehuck Woods Cave Room 1 Block 2", 0x39DD8A, 0xD407CC, 0),
    LocationData("Chucklehuck Woods Cave Room 2 Block", 0x39DD9F, 0xD407E1, 0),
    LocationData("Chucklehuck Woods Cave Room 3 Block", 0x39DDAC, 0xD407EE, 0),
    LocationData("Chucklehuck Woods Solo Luigi Cave Room 2 Block", 0x39DB72, 0xD405AC, 0),
    LocationData("Chucklehuck Woods Solo Luigi Cave Room 3 Block 1", 0x39DB5D, 0xD40597, 0),
    LocationData("Chucklehuck Woods Solo Luigi Cave Room 3 Block 2", 0x39DB65, 0xD4059F, 0),
    LocationData("Chucklehuck Woods Room 2 Block", 0x39DDC1, 0xD40803, 0),
    LocationData("Chucklehuck Woods Room 2 Digspot", 0x39DDC9, 0xD4080B, 0),
    LocationData("Chucklehuck Woods Pipe Room Block 1", 0x39DDD6, 0xD40818, 0),
    LocationData("Chucklehuck Woods Pipe Room Block 2", 0x39DDDE, 0xD40820, 0),
    LocationData("Chucklehuck Woods Pipe Room Digspot 1", 0x39DDEE, 0xD40830, 0),
    LocationData("Chucklehuck Woods Pipe Room Digspot 2", 0x39DDF6, 0xD40838, 0),
    LocationData("Chucklehuck Woods Room 4 Block 1", 0x39DE06, 0xD40848, 0),
    LocationData("Chucklehuck Woods Room 4 Block 2", 0x39DE0E, 0xD40850, 0),
    LocationData("Chucklehuck Woods Room 4 Block 3", 0x39DE16, 0xD40858, 0),
    LocationData("Chucklehuck Woods Room 7 Block 1", 0x39DE29, 0xD4086B, 0),
    LocationData("Chucklehuck Woods Room 7 Block 2", 0x39DE39, 0xD4087B, 0),
    LocationData("Chucklehuck Woods Room 7 Digspot 1", 0x39DE41, 0xD40883, 0),
    LocationData("Chucklehuck Woods Room 7 Digspot 2", 0x39DE49, 0xD4088B, 0),
    LocationData("Chucklehuck Woods Room 8 Digspot", 0x39DE56, 0xD408A0, 0),
    LocationData("Chucklehuck Woods East of Chuckleroot Digspot", 0x39DE66, 0xD408B0, 0),
    LocationData("Chucklehuck Woods Northeast of Chuckleroot Digspot 1", 0x39DE73, 0xD408BD, 0),
    LocationData("Chucklehuck Woods Northeast of Chuckleroot Digspot 2", 0x39DE7B, 0xD408C5, 0),
    LocationData("Chucklehuck Woods Northeast of Chuckleroot Digspot 3", 0x39DE83, 0xD408CD, 0),
    LocationData("Chucklehuck Woods Northeast of Chuckleroot Digspot 4", 0x39DE8B, 0xD408D5, 0),
    LocationData("Chucklehuck Woods White Fruit Room Digspot 1", 0x39DE98, 0xD408E2, 0),
    LocationData("Chucklehuck Woods White Fruit Room Digspot 2", 0x39DEA0, 0xD408EA, 0),
    LocationData("Chucklehuck Woods White Fruit Room Digspot 3", 0x39DEA8, 0xD408F2, 0),
    LocationData("Chucklehuck Woods West of Chuckleroot Block", 0x39DEB5, 0xD408FF, 0),
    LocationData("Chucklehuck Woods Southwest of Chuckleroot Block", 0x39DEC2, 0xD4090C, 0),
    LocationData("Chucklehuck Woods Wiggler room Digspot 1", 0x39DECF, 0xD40919, 0),
    LocationData("Chucklehuck Woods Wiggler room Digspot 2", 0x39DED7, 0xD40921, 0),
    LocationData("Chucklehuck Woods Past Chuckleroot Block 1", 0x39DEE4, 0xD4092E, 0),
    LocationData("Chucklehuck Woods Past Chuckleroot Block 2", 0x39DEEC, 0xD40936, 0),
    LocationData("Chucklehuck Woods Past Chuckleroot Block 3", 0x39DEF4, 0xD4093E, 0),
    LocationData("Chucklehuck Woods Past Chuckleroot Block 4", 0x39DEFC, 0xD40946, 0),
    LocationData("Chucklehuck Woods Past Chuckleroot Block 5", 0x39DF04, 0xD4094E, 0),
    LocationData("Chucklehuck Woods Past Chuckleroot Block 6", 0x39DF0C, 0xD40956, 0),
    LocationData("Chucklehuck Woods Koopa Room Block 1", 0x39DF4B, 0xD4099D, 0),
    LocationData("Chucklehuck Woods Koopa Room Block 2", 0x39DF5B, 0xD409AD, 0),
    LocationData("Chucklehuck Woods Koopa Room Digspot", 0x39DF63, 0xD409B5, 0),
    LocationData("Chucklehuck Woods Room 1 Digspot", 0x39E1C9, 0xD40C3F, 0),
    LocationData("Beanbean Outskirts Brooch Guards Room Digspot 1", 0x39E966, 0xD41486, 0),
    LocationData("Beanbean Outskirts Brooch Guards Room Digspot 2", 0x39E96E, 0xD4148E, 0),
    LocationData("Beanbean Outskirts Chateau Entrance Digspot 1", 0x39E97B, 0xD4149B, 0),
    LocationData("Beanbean Outskirts Chateau Entrance Digspot 2", 0x39E983, 0xD414A3, 0),
    LocationData("Chateau Green Goblet", 0x24E628, 0, 1),
    LocationData("Chateau Red Goblet", 0x1E943E, 0, 2),
    LocationData("Chucklehuck Woods Red Chuckola Fruit", 0x250621, 0, 2),
    LocationData("Chucklehuck Woods White Chuckola Fruit", 0x24FF18, 0, 2),
    LocationData("Chucklehuck Woods Purple Chuckola Fruit", 0x24ED74, 0, 1),
]

castleTown: typing.List[LocationData] = [
    LocationData("Beanbean Castle Town West Side House Block 1", 0x39D7A4, 0xD401AC, 0),
    LocationData("Beanbean Castle Town West Side House Block 2", 0x39D7AC, 0xD401B4, 0),
    LocationData("Beanbean Castle Town West Side House Block 3", 0x39D7B4, 0xD401BC, 0),
    LocationData("Beanbean Castle Town West Side House Block 4", 0x39D7BC, 0xD401C4, 0),
    LocationData("Beanbean Castle Town East Side House Block 1", 0x39D7D8, 0xD401E0, 0),
    LocationData("Beanbean Castle Town East Side House Block 2", 0x39D7E0, 0xD401E8, 0),
    LocationData("Beanbean Castle Town East Side House Block 3", 0x39D7E8, 0xD401F0, 0),
    LocationData("Beanbean Castle Town East Side House Block 4", 0x39D7F0, 0xD401F8, 0),
    LocationData("Beanbean Castle Peach's Extra Dress", 0x1E9433, 0, 2),
    LocationData("Beanbean Castle Fake Beanstar", 0x1E9432, 0, 2),
    LocationData("Beanbean Castle Town Beanlet 1", 0x251347, 0, 1),
    LocationData("Beanbean Castle Town Beanlet 2", 0x2513FB, 0, 1),
    LocationData("Beanbean Castle Town Beanlet 3", 0x2513A1, 0, 1),
    LocationData("Beanbean Castle Town Beanlet 4", 0x251988, 0, 1),
    LocationData("Beanbean Castle Town Beanlet 5", 0x25192E, 0, 1),
    LocationData("Beanbean Castle Town Beanstone 1", 0x25117D, 0, 1),
    LocationData("Beanbean Castle Town Beanstone 2", 0x2511D6, 0, 1),
    LocationData("Beanbean Castle Town Beanstone 3", 0x25122F, 0, 1),
    LocationData("Beanbean Castle Town Beanstone 4", 0x251288, 0, 1),
    LocationData("Beanbean Castle Town Beanstone 5", 0x2512E1, 0, 1),
    LocationData("Beanbean Castle Town Beanstone 6", 0x25170B, 0, 1),
    LocationData("Beanbean Castle Town Beanstone 7", 0x251767, 0, 1),
    LocationData("Beanbean Castle Town Beanstone 8", 0x2517C3, 0, 1),
    LocationData("Beanbean Castle Town Beanstone 9", 0x25181F, 0, 1),
    LocationData("Beanbean Castle Town Beanstone 10", 0x25187B, 0, 1),
    LocationData("Coffee Shop Brew Reward 1", 0x253515, 0, 1),
    LocationData("Coffee Shop Brew Reward 2", 0x253776, 0, 1),
    LocationData("Coffee Shop Brew Reward 3", 0x253C70, 0, 1),
    LocationData("Coffee Shop Brew Reward 4", 0x254324, 0, 1),
    LocationData("Coffee Shop Brew Reward 5", 0x254718, 0, 1),
    LocationData("Coffee Shop Brew Reward 6", 0x254A34, 0, 1),
    LocationData("Coffee Shop Brew Reward 7", 0x254E24, 0, 1),
    LocationData("Coffee Shop Woohoo Blend", 0x252D07, 0, 1),
    LocationData("Coffee Shop Hoohoo Blend", 0x252D28, 0, 1),
    LocationData("Coffee Shop Chuckle Blend", 0x252D49, 0, 1),
    LocationData("Coffee Shop Teehee Blend", 0x252D6A, 0, 1),
    LocationData("Coffee Shop Hoolumbian", 0x252D8B, 0, 1),
    LocationData("Coffee Shop Chuckoccino", 0x252DAC, 0, 1),
    LocationData("Coffee Shop Teeheespresso", 0x252DCD, 0, 1),
    LocationData("Beanbean Castle Town Beanstone Reward", 0x251071, 0, 1),
    LocationData("Beanbean Castle Town Beanlet Reward", 0x2515EB, 0, 1),
]

eReward: typing.List[int] = [0x253515, 0x253776, 0x253C70, 0x254324, 0x254718, 0x254A34, 0x254E24]

startingFlag: typing.List[LocationData] = [
    LocationData("Badge Shop Starting Flag 1", 0x3C0618, 0, 2),
    LocationData("Badge Shop Starting Flag 2", 0x3C061A, 0, 2),
    LocationData("Pants Shop Starting Flag 1", 0x3C061C, 0, 2),
    LocationData("Pants Shop Starting Flag 2", 0x3C061E, 0, 2),
    LocationData("Pants Shop Starting Flag 3", 0x3C0620, 0, 2),
]

chuckolatorFlag: typing.List[LocationData] = [
    LocationData("Shop Chuckolator Flag", 0x3C05F8, 0, 3),
    LocationData("Pants Shop Chuckolator Flag 1", 0x3C062A, 0, 2),
    LocationData("Pants Shop Chuckolator Flag 2", 0x3C062C, 0, 2),
    LocationData("Pants Shop Chuckolator Flag 3", 0x3C062E, 0, 2),
    LocationData("Badge Shop Chuckolator Flag 1", 0x3C0624, 0, 2),
    LocationData("Badge Shop Chuckolator Flag 2", 0x3C0626, 0, 2),
    LocationData("Badge Shop Chuckolator Flag 3", 0x3C0628, 0, 2),
]

piranhaFlag: typing.List[LocationData] = [
    LocationData("Shop Mom Piranha Flag 1", 0x3C05FC, 0, 3),
    LocationData("Shop Mom Piranha Flag 2", 0x3C05FE, 0, 3),
    LocationData("Shop Mom Piranha Flag 3", 0x3C0600, 0, 3),
    LocationData("Shop Mom Piranha Flag 4", 0x3C0602, 0, 3),
    LocationData("Pants Shop Mom Piranha Flag 1", 0x3C0638, 0, 2),
    LocationData("Pants Shop Mom Piranha Flag 2", 0x3C063A, 0, 2),
    LocationData("Pants Shop Mom Piranha Flag 3", 0x3C063C, 0, 2),
    LocationData("Badge Shop Mom Piranha Flag 1", 0x3C0632, 0, 2),
    LocationData("Badge Shop Mom Piranha Flag 2", 0x3C0634, 0, 2),
    LocationData("Badge Shop Mom Piranha Flag 3", 0x3C0636, 0, 2),
]

kidnappedFlag: typing.List[LocationData] = [
    LocationData("Badge Shop Trunkle Flag 1", 0x3C0640, 0, 2),
    LocationData("Badge Shop Trunkle Flag 2", 0x3C0642, 0, 2),
    LocationData("Badge Shop Trunkle Flag 3", 0x3C0644, 0, 2),
    LocationData("Pants Shop Trunkle Flag 1", 0x3C0646, 0, 2),
    LocationData("Pants Shop Trunkle Flag 2", 0x3C0648, 0, 2),
    LocationData("Pants Shop Trunkle Flag 3", 0x3C064A, 0, 2),
    LocationData("Shop Trunkle Flag 1", 0x3C0606, 0, 3),
    LocationData("Shop Trunkle Flag 2", 0x3C0608, 0, 3),
]

beanstarFlag: typing.List[LocationData] = [
    LocationData("Badge Shop Beanstar Complete Flag 1", 0x3C064E, 0, 2),
    LocationData("Badge Shop Beanstar Complete Flag 2", 0x3C0650, 0, 2),
    LocationData("Badge Shop Beanstar Complete Flag 3", 0x3C0652, 0, 2),
    LocationData("Pants Shop Beanstar Complete Flag 1", 0x3C0654, 0, 2),
    LocationData("Pants Shop Beanstar Complete Flag 2", 0x3C0656, 0, 2),
    LocationData("Pants Shop Beanstar Complete Flag 3", 0x3C0658, 0, 2),
    LocationData("Shop Beanstar Complete Flag 1", 0x3C060C, 0, 3),
    LocationData("Shop Beanstar Complete Flag 2", 0x3C060E, 0, 3),
    LocationData("Shop Beanstar Complete Flag 3", 0x3C0610, 0, 3),
]

birdoFlag: typing.List[LocationData] = [
    LocationData("Badge Shop Birdo Flag 1", 0x3C065C, 0, 2),
    LocationData("Badge Shop Birdo Flag 2", 0x3C065E, 0, 2),
    LocationData("Badge Shop Birdo Flag 3", 0x3C0660, 0, 2),
    LocationData("Pants Shop Birdo Flag 1", 0x3C0662, 0, 2),
    LocationData("Pants Shop Birdo Flag 2", 0x3C0664, 0, 2),
    LocationData("Pants Shop Birdo Flag 3", 0x3C0666, 0, 2),
    LocationData("Shop Birdo Flag", 0x3C0614, 0, 3),
]

winkle: typing.List[LocationData] = [
    LocationData("Chucklehuck Woods Winkle Cave Block 1", 0x39DF70, 0xD409C2, 0),
    LocationData("Chucklehuck Woods Winkle Cave Block 2", 0x39DF78, 0xD409CA, 0),
    LocationData("Winkle Area Beanstar Room Block", 0x39DF21, 0xD4096B, 0),
    LocationData("Winkle Area Digspot", 0x39DF2E, 0xD40978, 0),
    LocationData("Winkle Area Outside Colloseum Block", 0x39DF3B, 0xD4098D, 0),
    LocationData("Winkle Area Colloseum Digspot", 0x39E8A3, 0xD413B9, 0),
    LocationData("Beanstar Piece Winkle Area", 0x1E9440, 0, 2),
    LocationData("Winkle Area Winkle Card", 0x261658, 0, 1),
]

sewers: typing.List[LocationData] = [
    LocationData("Sewers Room 3 Block 1", 0x39DFE6, 0xD40A54, 0),
    LocationData("Sewers Room 3 Block 2", 0x39DFEE, 0xD40A5C, 0),
    LocationData("Sewers Room 3 Block 3", 0x39DFF6, 0xD40A64, 0),
    LocationData("Sewers Room 5 Block 1", 0x39E006, 0xD40A74, 0),
    LocationData("Sewers Room 5 Block 2", 0x39E00E, 0xD40A7C, 0),
    LocationData("Sewers Prison Room Block 1", 0x39E026, 0xD40A94, 0),
    LocationData("Sewers Prison Room Block 2", 0x39E02E, 0xD40A9C, 0),
    LocationData("Sewers Prison Room Block 3", 0x39E036, 0xD40AA4, 0),
    LocationData("Sewers Prison Room Block 4", 0x39E03E, 0xD40AAC, 0),
    LocationData("Beanbean Castle Beanbean Brooch", 0x2578E7, 0, 1),
]

hooniversity: typing.List[LocationData] = [
    LocationData("Woohoo Hooniversity South Of Star Room Block", 0x39E16F, 0xD40BDD, 0),
    LocationData("Woohoo Hooniversity Barrel Puzzle Entrance Digspot 1", 0x39E194, 0xD40C02, 0),
    LocationData("Woohoo Hooniversity Barrel Puzzle Entrance Block 1", 0x39E19C, 0xD40C0A, 0),
    LocationData("Woohoo Hooniversity Barrel Puzzle Entrance Block 2", 0x39E1A4, 0xD40C12, 0),
    LocationData("Woohoo Hooniversity Barrel Puzzle Entrance Block 3", 0x39E1AC, 0xD40C1A, 0),
    LocationData("Woohoo Hooniversity Barrel Puzzle Entrance Block 4", 0x39E1B4, 0xD40C22, 0),
    LocationData("Woohoo Hooniversity Barrel Puzzle Entrance Digspot 2", 0x39E1BC, 0xD40C2A, 0),
    LocationData("Woohoo Hooniversity Past Sun Door Block 1", 0x39E28C, 0xD40D12, 0),
    LocationData("Woohoo Hooniversity Past Sun Door Block 2", 0x39E294, 0xD40D1A, 0),
    LocationData("Woohoo Hooniversity Past Sun Door Block 3", 0x39E29C, 0xD40D22, 0),
    LocationData("Woohoo Hooniversity Past Cackletta Room 1 Block", 0x39E2AC, 0xD40D32, 0),
    LocationData("Woohoo Hooniversity Past Cackletta Room 2 Block 1", 0x39E2BF, 0xD40D59, 0),
    LocationData("Woohoo Hooniversity Past Cackletta Room 2 Block 2", 0x39E2C7, 0xD40D61, 0),
    LocationData("Woohoo Hooniversity Past Cackletta Room 2 Digspot", 0x39E2CF, 0xD40D69, 0),
    LocationData("Woohoo Hooniversity Basement Room 1 Digspot", 0x39E4C6, 0xD40F8C, 0),
    LocationData("Woohoo Hooniversity Basement Room 2 Digspot", 0x39E4D3, 0xD40F99, 0),
    LocationData("Woohoo Hooniversity Basement Room 3 Block", 0x39E4E0, 0xD40FA6, 0),
    LocationData("Woohoo Hooniversity Basement Room 4 Block", 0x39E4ED, 0xD40FB3, 0),
    LocationData("Woohoo Hooniversity Popple Room Digspot 1", 0x39E4FA, 0xD40FC0, 0),
    LocationData("Woohoo Hooniversity Popple Room Digspot 2", 0x39E502, 0xD40FC8, 0),
    LocationData("Woohoo Hooniversity Solo Mario Barrel Area Block 1", 0x39EC05, 0xD4177F, 0),
    LocationData("Woohoo Hooniversity Solo Mario Barrel Area Block 2", 0x39EC0D, 0xD41787, 0),
    LocationData("Woohoo Hooniversity Solo Mario Barrel Area Block 3", 0x39EC15, 0xD4178F, 0),
]

surfable: typing.List[LocationData] = [
    LocationData("Oho Ocean North Whirlpool Block 1", 0x39E0A5, 0xD40B13, 0),
    LocationData("Oho Ocean North Whirlpool Block 2", 0x39E0AD, 0xD40B1B, 0),
    LocationData("Oho Ocean North Whirlpool Block 3", 0x39E0B5, 0xD40B23, 0),
    LocationData("Oho Ocean North Whirlpool Block 4", 0x39E0BD, 0xD40B2B, 0),
    LocationData("Oho Ocean North Whirlpool Digspot 1", 0x39E0C5, 0xD40B33, 0),
    LocationData("Oho Ocean North Whirlpool Digspot 2", 0x39E0CD, 0xD40B3B, 0),
    LocationData("Oho Ocean Fire Puzzle Room Digspot", 0x39E057, 0xD40AC5, 0),
    LocationData("Oho Ocean South Whirlpool Digspot 1", 0x39E0DA, 0xD40B48, 0),
    LocationData("Oho Ocean South Whirlpool Digspot 2", 0x39E0E2, 0xD40B50, 0),
    LocationData("Oho Ocean South Whirlpool Digspot 3", 0x39E0EA, 0xD40B58, 0),
    LocationData("Oho Ocean South Whirlpool Digspot 4", 0x39E0F2, 0xD40B60, 0),
    LocationData("Oho Ocean South Whirlpool Digspot 5", 0x39E0FA, 0xD40B68, 0),
    LocationData("Oho Ocean South Whirlpool Digspot 6", 0x39E102, 0xD40B70, 0),
    LocationData("Oho Ocean South Whirlpool Room 2 Digspot", 0x39E10F, 0xD40B7D, 0),
    LocationData("Joke's End Pipe Digspot", 0x39E6C2, 0xD4119A, 0),
    LocationData("Joke's End Staircase Digspot", 0x39E6CF, 0xD411A7, 0),
    LocationData("Surf Minigame", 0x2753EA, 0, 1),
    LocationData("North Ocean Whirlpool Mole", 0x277956, 0, 1),
    LocationData("Beanbean Outskirts Surf Beach Digspot 1", 0x39DCFB, 0xD40735, 0),
    LocationData("Beanbean Outskirts Surf Beach Digspot 2", 0x39DD0B, 0xD40745, 0),
    LocationData("Beanbean Outskirts Surf Beach Digspot 3", 0x39DD13, 0xD4074D, 0),
]

airport: typing.List[LocationData] = [
    LocationData("Airport Entrance Digspot", 0x39E2DC, 0xD40D76, 0),
    LocationData("Airport Lobby Digspot", 0x39E2E9, 0xD40D8B, 0),
    LocationData("Airport Westside Digspot 1", 0x39E2F6, 0xD40D98, 0),
    LocationData("Airport Westside Digspot 2", 0x39E2FE, 0xD40DA0, 0),
    LocationData("Airport Westside Digspot 3", 0x39E306, 0xD40DA8, 0),
    LocationData("Airport Westside Digspot 4", 0x39E30E, 0xD40DB0, 0),
    LocationData("Airport Westside Digspot 5", 0x39E316, 0xD40DB8, 0),
    LocationData("Airport Center Digspot 1", 0x39E323, 0xD40DCD, 0),
    LocationData("Airport Center Digspot 2", 0x39E32B, 0xD40DD5, 0),
    LocationData("Airport Center Digspot 3", 0x39E333, 0xD40DDD, 0),
    LocationData("Airport Center Digspot 4", 0x39E33B, 0xD40DE5, 0),
    LocationData("Airport Center Digspot 5", 0x39E343, 0xD40DED, 0),
    LocationData("Airport Eastside Digspot 1", 0x39E350, 0xD40DFA, 0),
    LocationData("Airport Eastside Digspot 2", 0x39E358, 0xD40E02, 0),
    LocationData("Airport Eastside Digspot 3", 0x39E360, 0xD40E0A, 0),
    LocationData("Airport Eastside Digspot 4", 0x39E368, 0xD40E12, 0),
    LocationData("Airport Eastside Digspot 5", 0x39E370, 0xD40E1A, 0),
]

gwarharEntrance: typing.List[LocationData] = [
    LocationData("Gwarhar Lagoon Pipe Room Digspot", 0x39E37D, 0xD40E27, 0),
    LocationData("Gwarhar Lagoon Massage Parlor Entrance Digspot", 0x39E396, 0xD40E4A, 0),
    LocationData("Gwarhar Lagoon First Underwater Area Room 1 Block", 0x39E438, 0xD40EFE, 0),
    LocationData("Gwarhar Lagoon First Underwater Area Room 2 Block 1", 0x39E445, 0xD40F0B, 0),
    LocationData("Gwarhar Lagoon First Underwater Area Room 2 Block 2", 0x39E44D, 0xD40F13, 0),
    LocationData("Gwarhar Lagoon Red Pearl Bean", 0x235C1C, 0, 1),
    LocationData("Gwarhar Lagoon Green Pearl Bean", 0x235A5B, 0, 1),
    LocationData("Oho Ocean South Room 1 Block", 0x39E06A, 0xD40AD8, 0),
    LocationData("Oho Ocean South Room 2 Digspot", 0x39E077, 0xD40AE5, 0),
]

gwarharMain: typing.List[LocationData] = [
    LocationData("Gwarhar Lagoon Past Hermie Digspot", 0x39E3A6, 0xD40E62, 0),
    LocationData("Gwarhar Lagoon East of Stone Bridge Block", 0x39E403, 0xD40EC9, 0),
    LocationData("Gwarhar Lagoon North of Spangle Room Digspot", 0x39E40B, 0xD40ED1, 0),
    LocationData("Gwarhar Lagoon West of Spangle Room Digspot", 0x39E41B, 0xD40EE1, 0),
    LocationData("Gwarhar Lagoon Second Underwater Area Room 4 Digspot", 0x39E462, 0xD40F28, 0),
    LocationData("Gwarhar Lagoon Second Underwater Area Room 2 Digspot 1", 0x39E46F, 0xD40F35, 0),
    LocationData("Gwarhar Lagoon Second Underwater Area Room 2 Digspot 2", 0x39E477, 0xD40F3D, 0),
    LocationData("Gwarhar Lagoon Second Underwater Area Room 3 Block 1", 0x39E484, 0xD40F4A, 0),
    LocationData("Gwarhar Lagoon Second Underwater Area Room 3 Block 2", 0x39E48C, 0xD40F52, 0),
    LocationData("Gwarhar Lagoon Second Underwater Area Room 3 Block 3", 0x39E494, 0xD40F5A, 0),
    LocationData("Gwarhar Lagoon Second Underwater Area Room 1 Block", 0x39E4A1, 0xD40F67, 0),
    LocationData("Gwarhar Lagoon Entrance to West Underwater Area Digspot", 0x39E3BC, 0xD40E82, 0),
    LocationData("Gwarhar Lagoon Fire Dash Puzzle Room 1 Digspot 1", 0x39E3C9, 0xD40E8F, 0),
    LocationData("Gwarhar Lagoon Fire Dash Puzzle Room 1 Digspot 2", 0x39E3D1, 0xD40E97, 0),
    LocationData("Gwarhar Lagoon Fire Dash Puzzle Room 2 Digspot", 0x39E3DE, 0xD40EA4, 0),
    LocationData("Gwarhar Lagoon Fire Dash Puzzle Room 3 Digspot 1", 0x39E3EB, 0xD40EB1, 0),
    LocationData("Gwarhar Lagoon Fire Dash Puzzle Room 3 Digspot 2", 0x39E3F3, 0xD40EB9, 0),
    LocationData("Gwarhar Lagoon Spangle Room Block", 0x39E428, 0xD40EEE, 0),
    LocationData("Gwarhar Lagoon Spangle Reward", 0x236E73, 0, 1),
    LocationData("Beanstar Piece Hermie", 0x1E9443, 0, 2),
    LocationData("Gwarhar Lagoon Spangle", 0x1E9437, 0, 2),
]

teeheeValley: typing.List[LocationData] = [
    LocationData("Teehee Valley Room 1 Digspot 1", 0x39E51E, 0xD40FE4, 0),
    LocationData("Teehee Valley Room 1 Digspot 2", 0x39E526, 0xD40FEC, 0),
    LocationData("Teehee Valley Room 1 Digspot 3", 0x39E52E, 0xD40FF4, 0),
    LocationData("Teehee Valley Room 2 Digspot 1", 0x39E53B, 0xD41001, 0),
    LocationData("Teehee Valley Room 2 Digspot 2", 0x39E543, 0xD41009, 0),
    LocationData("Teehee Valley Room 2 Digspot 3", 0x39E54B, 0xD41011, 0),
    LocationData("Teehee Valley Past Ultra Hammer Rock Block 1", 0x39E580, 0xD4104E, 0),
    LocationData("Teehee Valley Past Ultra Hammer Rock Block 2", 0x39E590, 0xD4105E, 0),
    LocationData("Teehee Valley Past Ultra Hammer Rock Digspot 1", 0x39E598, 0xD41066, 0),
    LocationData("Teehee Valley Past Ultra Hammer Rock Digspot 3", 0x39E5A8, 0xD41076, 0),
    LocationData("Teehee Valley Before Trunkle Digspot", 0x39E5F0, 0xD410BE, 0),
    LocationData("S.S. Chuckola Storage Room Block 1", 0x39E610, 0xD410DE, 0),
    LocationData("S.S. Chuckola Storage Room Block 2", 0x39E628, 0xD410F6, 0),
    LocationData("S.S. Chuckola Membership Card", 0x260637, 0, 1),
]

fungitown: typing.List[LocationData] = [
    LocationData("Teehee Valley Trunkle Room Digspot", 0x39E5FD, 0xD410CB, 0),
    LocationData("Fungitown Embassy Room Block", 0x39E66B, 0xD41143, 0),
    LocationData("Fungitown Entrance Room Block", 0x39E67E, 0xD41156, 0),
    LocationData("Fungitown Badge Shop Starting Flag 1", 0x3C0684, 0, 2),
    LocationData("Fungitown Badge Shop Starting Flag 2", 0x3C0686, 0, 2),
    LocationData("Fungitown Badge Shop Starting Flag 3", 0x3C0688, 0, 2),
    LocationData("Fungitown Shop Starting Flag 1", 0x3C066A, 0, 3),
    LocationData("Fungitown Shop Starting Flag 2", 0x3C066C, 0, 3),
    LocationData("Fungitown Shop Starting Flag 3", 0x3C066E, 0, 3),
    LocationData("Fungitown Shop Starting Flag 4", 0x3C0670, 0, 3),
    LocationData("Fungitown Shop Starting Flag 5", 0x3C0672, 0, 3),
    LocationData("Fungitown Shop Starting Flag 6", 0x3C0674, 0, 3),
    LocationData("Fungitown Shop Starting Flag 7", 0x3C0676, 0, 3),
    LocationData("Fungitown Shop Starting Flag 8", 0x3C0678, 0, 3),
    LocationData("Fungitown Pants Shop Starting Flag 1", 0x3C068A, 0, 2),
    LocationData("Fungitown Pants Shop Starting Flag 2", 0x3C068C, 0, 2),
    LocationData("Fungitown Pants Shop Starting Flag 3", 0x3C068E, 0, 2),
]

fungitownBeanstar: typing.List[LocationData] = [
    LocationData("Fungitown Badge Shop Beanstar Complete Flag 1", 0x3C0692, 0, 2),
    LocationData("Fungitown Badge Shop Beanstar Complete Flag 2", 0x3C0694, 0, 2),
    LocationData("Fungitown Pants Shop Beanstar Complete Flag 1", 0x3C0696, 0, 2),
    LocationData("Fungitown Pants Shop Beanstar Complete Flag 2", 0x3C0698, 0, 2),
    LocationData("Fungitown Shop Beanstar Complete Flag", 0x3C067C, 0, 3),
]

fungitownBirdo: typing.List[LocationData] = [
    LocationData("Fungitown Shop Birdo Flag", 0x3C0680, 0, 3),
    LocationData("Fungitown Pants Shop Birdo Flag 1", 0x3C06A0, 0, 2),
    LocationData("Fungitown Pants Shop Birdo Flag 2", 0x3C06A2, 0, 2),
    LocationData("Fungitown Badge Shop Birdo Flag 1", 0x3C069C, 0, 2),
    LocationData("Fungitown Badge Shop Birdo Flag 2", 0x3C069E, 0, 2),
]

bowsers: typing.List[LocationData] = [
    LocationData("Bowser's Castle Entrance Block 1", 0x39E9D2, 0xD414F2, 0),
    LocationData("Bowser's Castle Entrance Block 2", 0x39E9DA, 0xD414FA, 0),
    LocationData("Bowser's Castle Entrance Digspot", 0x39E9E2, 0xD41502, 0),
    LocationData("Bowser's Castle Iggy & Morton Hallway Block 1", 0x39E9EF, 0xD4150F, 0),
    LocationData("Bowser's Castle Iggy & Morton Hallway Block 2", 0x39E9F7, 0xD41517, 0),
    LocationData("Bowser's Castle Iggy & Morton Hallway Digspot", 0x39E9FF, 0xD4151F, 0),
    LocationData("Bowser's Castle Past Morton Block", 0x39EA0C, 0xD4152C, 0),
    LocationData("Bowser's Castle Morton Room 1 Digspot", 0x39EA89, 0xD415A9, 0),
    LocationData("Bowser's Castle Lemmy Room 1 Block", 0x39EA9C, 0xD415BC, 0),
    LocationData("Bowser's Castle Lemmy Room 1 Digspot", 0x39EAA4, 0xD415C4, 0),
    LocationData("Bowser's Castle Ludwig Room 1 Block", 0x39EABA, 0xD415E2, 0),
    LocationData("Bowser's Castle Lemmy Room Mole", 0x277B1F, 0, 1),
]

bowsersMini: typing.List[LocationData] = [
    LocationData("Bowser's Castle Ludwig & Roy Hallway Block 1", 0x39EA1C, 0xD4153C, 0),
    LocationData("Bowser's Castle Ludwig & Roy Hallway Block 2", 0x39EA24, 0xD41544, 0),
    LocationData("Bowser's Castle Roy Corridor Block 1", 0x39EA31, 0xD41551, 0),
    LocationData("Bowser's Castle Roy Corridor Block 2", 0x39EA39, 0xD41559, 0),
    LocationData("Bowser's Castle Mini Mario Sidescroller Block 1", 0x39EAD6, 0xD41608, 0),
    LocationData("Bowser's Castle Mini Mario Sidescroller Block 2", 0x39EADE, 0xD41610, 0),
    LocationData("Bowser's Castle Mini Mario Maze Block 1", 0x39EAEB, 0xD4161D, 0),
    LocationData("Bowser's Castle Mini Mario Maze Block 2", 0x39EAF3, 0xD41625, 0),
    LocationData("Bowser's Castle Before Wendy Fight Block 1", 0x39EB12, 0xD4164E, 0),
    LocationData("Bowser's Castle Before Wendy Fight Block 2", 0x39EB1A, 0xD41656, 0),
    LocationData("Bowser's Castle Larry Room Block", 0x39EBB6, 0xD416F2, 0),
    LocationData("Bowser's Castle Wendy & Larry Hallway Digspot", 0x39EA46, 0xD41566, 0),
    LocationData("Bowser's Castle Before Fawful Fight Block 1", 0x39EA56, 0xD41576, 0),
    LocationData("Bowser's Castle Before Fawful Fight Block 2", 0x39EA5E, 0xD4157E, 0),
    LocationData("Bowser's Castle Great Door Block 1", 0x39EA6B, 0xD4158B, 0),
    LocationData("Bowser's Castle Great Door Block 2", 0x39EA73, 0xD41593, 0),
]

jokesEntrance: typing.List[LocationData] = [
    LocationData("Joke's End West of First Boiler Room Block 1", 0x39E6E5, 0xD411BD, 0),
    LocationData("Joke's End West of First Boiler Room Block 2", 0x39E6ED, 0xD411C5, 0),
    LocationData("Joke's End First Boiler Room Digspot 1", 0x39E6FA, 0xD411DA, 0),
    LocationData("Joke's End First Boiler Room Digspot 2", 0x39E702, 0xD411E2, 0),
    LocationData("Joke's End Second Floor West Room Block 1", 0x39E761, 0xD41251, 0),
    LocationData("Joke's End Second Floor West Room Block 2", 0x39E769, 0xD41259, 0),
    LocationData("Joke's End Second Floor West Room Block 3", 0x39E779, 0xD41269, 0),
    LocationData("Joke's End Second Floor West Room Block 4", 0x39E781, 0xD41271, 0),
    LocationData("Joke's End Mole Reward 1", 0x27788E, 0, 1),
    LocationData("Joke's End Mole Reward 2", 0x2778D2, 0, 1),
    LocationData("Joke's End Furnace Room 1 Block 1", 0x39E70F, 0xD411EF, 0),
    LocationData("Joke's End Furnace Room 1 Block 2", 0x39E717, 0xD411F7, 0),
    LocationData("Joke's End Furnace Room 1 Block 3", 0x39E71F, 0xD411FF, 0),
    LocationData("Joke's End Northeast of Boiler Room 1 Block", 0x39E732, 0xD41212, 0),
    LocationData("Joke's End Northeast of Boiler Room 2 Block", 0x39E74C, 0xD41234, 0),
    LocationData("Joke's End Northeast of Boiler Room 2 Digspot", 0x39E754, 0xD4123C, 0),
    LocationData("Joke's End Northeast of Boiler Room 3 Digspot", 0x39E73F, 0xD4121F, 0),
]

jokesMain: typing.List[LocationData] = [
    LocationData("Joke's End Second Floor East Room Digspot", 0x39E794, 0xD41284, 0),
    LocationData("Joke's End Final Split up Room Digspot", 0x39E7A7, 0xD41297, 0),
    LocationData("Joke's End South of Bridge Room Block", 0x39E7B4, 0xD412A4, 0),
    LocationData("Joke's End Solo Luigi Room 1 Block", 0x39E7C4, 0xD412B4, 0),
    LocationData("Joke's End Solo Luigi Room 1 Digspot", 0x39E7CC, 0xD412BC, 0),
    LocationData("Joke's End Solo Mario Final Room Block 1", 0x39E7D9, 0xD412C9, 0),
    LocationData("Joke's End Solo Mario Final Room Block 2", 0x39E7E1, 0xD412D1, 0),
    LocationData("Joke's End Solo Mario Final Room Block 3", 0x39E7E9, 0xD412D9, 0),
    LocationData("Joke's End Solo Luigi Room 2 Digspot", 0x39E7FC, 0xD412EC, 0),
    LocationData("Joke's End Solo Mario Room 1 Digspot", 0x39E809, 0xD412F9, 0),
    LocationData("Joke's End Solo Mario Room 2 Block 1", 0x39E819, 0xD41309, 0),
    LocationData("Joke's End Solo Mario Room 2 Block 2", 0x39E821, 0xD41311, 0),
    LocationData("Joke's End Solo Mario Room 2 Block 3", 0x39E829, 0xD41319, 0),
    LocationData("Joke's End Second Boiler Room Digspot 1", 0x39E84F, 0xD41349, 0),
    LocationData("Joke's End Second Boiler Room Digspot 2", 0x39E857, 0xD41351, 0),
    LocationData("Joke's End North of Second Boiler Room Block 1", 0x39E864, 0xD4135E, 0),
    LocationData("Joke's End North of Second Boiler Room Block 2", 0x39E86C, 0xD41366, 0),
    LocationData("Joke's End Before Jojora Room Block 1", 0x39E927, 0xD41447, 0),
    LocationData("Joke's End Before Jojora Room Block 2", 0x39E92F, 0xD4144F, 0),
    LocationData("Joke's End Before Jojora Room Digspot", 0x39E937, 0xD41457, 0),
    LocationData("Joke's End Jojora Room Digspot", 0x39E944, 0xD41464, 0),
]

postJokes: typing.List[LocationData] = [
    LocationData("Teehee Valley Past Ultra Hammer Rock Digspot 2 (Post-Birdo)", 0x39E5A0, 0xD4106E, 0),
    LocationData("Teehee Valley Before Birdo Digspot 1", 0x39E55B, 0xD41029, 0),
    LocationData("Teehee Valley Before Birdo Digspot 2", 0x39E563, 0xD41031, 0),
    LocationData("Teehee Valley Before Birdo Digspot 3", 0x39E56B, 0xD41039, 0),
    LocationData("Teehee Valley Before Birdo Digspot 4", 0x39E573, 0xD41041, 0),
]

theater: typing.List[LocationData] = [
    LocationData("Yoshi Theater Blue Yoshi", 0x241155, 0, 1),
    LocationData("Yoshi Theater Red Yoshi", 0x240EBE, 0, 1),
    LocationData("Yoshi Theater Green Yoshi", 0x241AFA, 0, 1),
    LocationData("Yoshi Theater Yellow Yoshi", 0x241C3C, 0, 1),
    LocationData("Yoshi Theater Purple Yoshi", 0x241297, 0, 1),
    LocationData("Yoshi Theater Orange Yoshi", 0x241000, 0, 1),
    LocationData("Yoshi Theater Azure Yoshi", 0x241D7E, 0, 1),
    LocationData("Beanstar Piece Yoshi Theater", 0x1E9442, 0, 2),
]

oasis: typing.List[LocationData] = [
    LocationData("Oho Oasis West Digspot", 0x39DF9F, 0xD40A03, 0),
    LocationData("Oho Oasis Fire Palace Block", 0x39DFBE, 0xD40A22, 0),
    LocationData("Oho Ocean Spike Room Digspot 1", 0x39E08A, 0xD40AF8, 0),
    LocationData("Oho Ocean Spike Room Digspot 2", 0x39E092, 0xD40B00, 0),
    LocationData("Oho Oasis Firebrand", 0x1E9408, 0, 2),
    LocationData("Oho Oasis Thunderhand", 0x1E9409, 0, 2),
]

cacklettas_soul: typing.List[LocationData] = [
    LocationData("Cackletta's Soul", None, None, 0),
]

nonBlock = [
    (0x434B, 0x1, 0x243844),  # Farm Mole 1
    (0x434B, 0x1, 0x24387D),  # Farm Mole 2
    (0x4373, 0x8, 0x2779C8),  # Simulblock Mole
    (0x42F9, 0x4, 0x1E9403),  # Hammers
    (0x434B, 0x10, 0x1E9435),  # Solo Mario Mole 1
    (0x434B, 0x20, 0x1E9436),  # Solo Mario Mole 2
    (0x4359, 0x20, 0x1E9404),  # Super Hammers
    (0x4359, 0x40, 0x1E9405),  # Ultra Hammers
    (0x42F9, 0x2, 0x1E9430),  # Rose
    (0x434B, 0x4, 0x242888),  # Solo Luigi Cave Mole
    (0x4373, 0x20, 0x277AB2),  # Hoohoo Village Turtle Mole
    (0x432D, 0x20, 0x1E9431),  # Piranha Bean
    (0x434E, 0x2, 0x1E9411),  # Secret Scroll 1
    (0x434E, 0x4, 0x1E9412),  # Secret Scroll 2
    (0x4375, 0x8, 0x260637),  # Membership Card
    (0x4373, 0x10, 0x277A45),  # Teehee Valley Mole
    (0x434D, 0x8, 0x1E9444),  # Harhall's Pants
    (0x432E, 0x10, 0x1E9441),  # Harhall Beanstar Piece
    (0x434B, 0x8, 0x1E9434),  # Outskirts Boostatue Mole
    (0x42FE, 0x2, 0x1E943E),  # Red Goblet
    (0x42FE, 0x4, 0x24E628),  # Green Goblet
    (0x4301, 0x10, 0x250621),  # Red Chuckola Fruit
    (0x42FE, 0x80, 0x24ED74),  # Purple Chuckola Fruit
    (0x4302, 0x4, 0x24FF18),  # White Chuckola Fruit
    (0x42FF, 0x8, 0x251347),  # Beanlet 1
    (0x42FF, 0x20, 0x2513FB),  # Beanlet 2
    (0x42FF, 0x10, 0x2513A1),  # Beanlet 3
    (0x42FF, 0x4, 0x251988),  # Beanlet 4
    (0x42FF, 0x2, 0x25192E),  # Beanlet 5
    (0x42FF, 0x1, 0x2515EB),  # Beanlet Reward
    (0x4371, 0x40, 0x253515),  # Espresso 1
    (0x4371, 0x80, 0x253776),  # Espresso 2
    (0x4372, 0x1, 0x253C70),  # Espresso 3
    (0x4372, 0x2, 0x254324),  # Espresso 4
    (0x4372, 0x4, 0x254718),  # Espresso 5
    (0x4372, 0x8, 0x254A34),  # Espresso 6
    (0x4372, 0x10, 0x254E24),  # Espresso 7
    (0x472F, 0x1, 0x252D07),  # Woohoo Blend
    (0x472F, 0x2, 0x252D28),  # Hoohoo Blend
    (0x472F, 0x4, 0x252D49),  # Chuckle Blend
    (0x472F, 0x8, 0x252D6A),  # Teehee Blend
    (0x472F, 0x10, 0x252D8B),  # Hoolumbian
    (0x472F, 0x20, 0x252DAC),  # Chuckoccino
    (0x472F, 0x40, 0x252DCD),  # Teeheespresso
    (0x430B, 0x10, 0x1E9433),  # Extra Dress
    (0x430B, 0x10, 0x1E9432),  # Fake Beanstar
    (0x430F, 0x1, 0x1E9440),  # Popple Beanstar Piece
    (0x467E, 0xFF, 0x261658),  # Winkle Card
    (0x4300, 0x40, 0x2578E7),  # Brooch
    (0x4375, 0x2, 0x2753EA),  # Surf Minigame
    (0x4373, 0x1, 0x277956),  # North Whirlpool Mole
    (0x4346, 0x40, 0x235A5B),  # Green Pearl Bean
    (0x4346, 0x80, 0x235C1C),  # Red Pearl Bean
    (0x4340, 0x20, 0x1E9443),  # Hermie Beanstar Piece
    (0x434A, 0x40, 0x1E9437),  # Spangle
    (0x434A, 0x80, 0x236E73),  # Spangle Reward
    (0x4373, 0x40, 0x277B1F),  # Bowser's Castle Mole
    (0x4372, 0x80, 0x27788E),  # Jokes end Mole 1
    (0x4372, 0x80, 0x2778D2),  # Jokes end Mole 2
    (0x434C, 0x80, 0x241000),  # Orange Neon Egg
    (0x434D, 0x1, 0x240EBE),  # Red Neon Egg
    (0x434C, 0x40, 0x241155),  # Blue Neon Egg
    (0x434D, 0x2, 0x241297),  # Purple Neon Egg
    (0x434C, 0x8, 0x241AFA),  # Green Neon Egg
    (0x434C, 0x10, 0x241D7E),  # Azure Neon Egg
    (0x434C, 0x20, 0x241C3C),  # Yellow Neon Egg
    (0x4406, 0x8, 0x1E9442),  # Theater Beanstar Piece
    (0x4345, 0x8, 0x1E9408),  # Firebrand
    (0x4345, 0x4, 0x1E9409),  # Thunder Hand
    (0x42FF, 0x80, 0x251071),  # Beanstone Reward
    (0x42F9, 0x2, 0xDA0000),  # Dragohoho
    (0x433D, 0x1, 0xDA0001),  # Chuckolator
    (0x43FC, 0x80, 0xDA0002),  # Popple 2
    (0x433D, 0x2, 0xDA0003),  # Mom Piranha
    (0x4342, 0x10, 0xDA0004),  # Fungitowm
    (0x433D, 0x8, 0xDA0005),  # Beanstar
    (0x430F, 0x40, 0xDA0006),  # Jojora
    (0x433D, 0x10, 0xDA0007),  # Birdo
]

roomException = {
    0x1E9437: [0xFE, 0xFF, 0x100],
    0x24ED74: [0x94, 0x95, 0x96, 0x99],
    0x250621: [0x94, 0x95, 0x96, 0x99],
    0x24FF18: [0x94, 0x95, 0x96, 0x99],
    0x260637: [0x135],
    0x1E9403: [0x4D],
    0xDA0001: [0x79, 0x192, 0x193],
    0x2578E7: [0x79, 0x192, 0x193],
}

beanstones = {
    0x229345: 0x39DC72, # Bean fruit 1 - 6
    0x22954D: 0x39DCB4,
    0x228A17: 0x39DBD1,
    0x22913A: 0x39DC10,
    0x22890E: 0x39DBA4,
    0x228775: 0x39DB7F,
    0x251288: 0x39D73E, # Beanstone 1 - 10
    0x2512E1: 0x39D746,
    0x25122F: 0x39D74E,
    0x25117D: 0x39D756,
    0x2511D6: 0x39D75E,
    0x25187B: 0x39D76B,
    0x25170B: 0x39D773,
    0x251767: 0x39D77B,
    0x2517C3: 0x39D783,
    0x25181F: 0x39D78B,
}

roomCount = {
    0x15: 2,
    0x18: 4,
    0x19: 3,
    0x1A: 3,
    0x1B: 2,
    0x1E: 1,
    0x23: 3,
    0x27: 1,
    0x28: 5,
    0x29: 5,
    0x2E: 4,
    0x34: 4,
    0x37: 1,
    0x39: 5,
    0x44: 1,
    0x45: 4,
    0x46: 3,
    0x47: 4,
    0x48: 3,
    0x4A: 2,
    0x4B: 2,
    0x4C: 3,
    0x4D: 2,
    0x51: 2,
    0x53: 5,
    0x54: 5,
    0x55: 5,
    0x56: 2,
    0x57: 1,
    0x58: 2,
    0x59: 2,
    0x5A: 3,
    0x63: 2,
    0x68: 2,
    0x69: 2,
    0x6B: 3,
    0x6C: 5,
    0x6D: 1,
    0x70: 3,
    0x74: 2,
    0x75: 2,
    0x76: 1,
    0x77: 4,
    0x78: 4,
    0x79: 4,
    0x7A: 1,
    0x7B: 1,
    0x7C: 5,
    0x7D: 7,
    0x7E: 3,
    0x7F: 3,
    0x80: 4,
    0x81: 3,
    0x82: 1,
    0x83: 4,
    0x84: 1,
    0x86: 5,
    0x87: 1,
    0x89: 1,
    0x8A: 3,
    0x8B: 2,
    0x8C: 2,
    0x8D: 2,
    0x8E: 5,
    0x90: 3,
    0x93: 5,
    0x94: 1,
    0x96: 1,
    0x97: 4,
    0x98: 3,
    0x99: 1,
    0x9A: 1,
    0x9B: 2,
    0x9C: 7,
    0x9D: 1,
    0x9E: 1,
    0x9F: 1,
    0xA1: 4,
    0xA2: 3,
    0xA9: 1,
    0xB0: 1,
    0xBA: 3,
    0xBC: 2,
    0xBE: 5,
    0xC3: 1,
    0xC6: 1,
    0xC7: 1,
    0xCA: 2,
    0xCD: 6,
    0xCE: 6,
    0xCF: 1,
    0xDB: 3,
    0xDC: 2,
    0xDD: 1,
    0xDF: 2,
    0xE0: 6,
    0xE1: 1,
    0xE2: 1,
    0xE3: 1,
    0xE4: 5,
    0xE5: 1,
    0xE6: 2,
    0xE7: 1,
    0xE8: 2,
    0xE9: 4,
    0xEC: 3,
    0xEE: 1,
    0xF1: 3,
    0xF2: 1,
    0xF3: 1,
    0xF4: 5,
    0xF5: 5,
    0xF6: 5,
    0xF7: 1,
    0xFC: 1,
    0xFE: 1,
    0x102: 1,
    0x103: 2,
    0x104: 1,
    0x105: 2,
    0x107: 2,
    0x109: 1,
    0x10A: 1,
    0x10C: 1,
    0x10D: 3,
    0x10E: 1,
    0x10F: 2,
    0x110: 3,
    0x111: 1,
    0x112: 2,
    0x114: 1,
    0x115: 1,
    0x116: 1,
    0x117: 1,
    0x118: 2,
    0x11E: 3,
    0x11F: 3,
    0x121: 4,
    0x122: 6,
    0x123: 1,
    0x126: 2,
    0x128: 1,
    0x12A: 1,
    0x12B: 1,
    0x12E: 4,
    0x139: 2,
    0x13B: 1,
    0x13E: 1,
    0x147: 1,
    0x14E: 1,
    0x14F: 1,
    0x153: 2,
    0x154: 2,
    0x155: 3,
    0x158: 1,
    0x159: 1,
    0x15A: 2,
    0x15B: 5,
    0x15E: 1,
    0x161: 1,
    0x162: 1,
    0x164: 2,
    0x165: 3,
    0x168: 1,
    0x169: 1,
    0x16B: 3,
    0x16C: 1,
    0x171: 2,
    0x172: 2,
    0x181: 1,
    0x186: 3,
    0x187: 1,
    0x18D: 2,
    0x18E: 3,
    0x18F: 3,
    0x190: 1,
    0x191: 2,
    0x192: 2,
    0x193: 2,
    0x194: 3,
    0x195: 4,
    0x196: 3,
    0x197: 3,
    0x198: 1,
    0x19A: 2,
    0x19B: 2,
    0x19C: 1,
    0x19E: 2,
    0x19F: 2,
    0x1A3: 1,
    0x1A6: 2,
    0x1AA: 1,
    0x1B0: 2,
    0x1B1: 2,
    0x1B8: 2,
    0x1CA: 2,
    0x1D1: 2,
    0x1D2: 3,
    0x1D4: 1,
    0x1EB: 3,
    0x1F6: 1,
    0x1F7: 1,
}

shop = {
    0x3C05F0: [
        0x3C05F0,
        0x3C05F2,
        0x3C05F4,
        0x3C05F8,
        0x3C05FC,
        0x3C05FE,
        0x3C0600,
        0x3C0602,
        0x3C0606,
        0x3C0608,
        0x3C060C,
        0x3C060E,
        0x3C0610,
        0x3C0614,
    ],
    0x3C066A: [0x3C066A, 0x3C066C, 0x3C066E, 0x3C0670, 0x3C0672, 0x3C0674, 0x3C0676, 0x3C0678, 0x3C067C, 0x3C0680],
}

badge = {
    0x3C0618: [
        0x3C0618,
        0x3C061A,
        0x3C0624,
        0x3C0626,
        0x3C0628,
        0x3C0632,
        0x3C0634,
        0x3C0636,
        0x3C0640,
        0x3C0642,
        0x3C0644,
        0x3C064E,
        0x3C0650,
        0x3C0652,
        0x3C065C,
        0x3C065E,
        0x3C0660,
    ],
    0x3C0684: [0x3C0684, 0x3C0686, 0x3C0688, 0x3C0692, 0x3C0694, 0x3C069C, 0x3C069E],
}

pants = {
    0x3C0618: [
        0x3C061C,
        0x3C061E,
        0x3C0620,
        0x3C062A,
        0x3C062C,
        0x3C062E,
        0x3C0638,
        0x3C063A,
        0x3C063C,
        0x3C0646,
        0x3C0648,
        0x3C064A,
        0x3C0654,
        0x3C0656,
        0x3C0658,
        0x3C0662,
        0x3C0664,
        0x3C0666,
    ],
    0x3C0684: [0x3C068A, 0x3C068C, 0x3C068E, 0x3C0696, 0x3C0698, 0x3C06A0, 0x3C06A2],
}

all_locations: typing.List[LocationData] = (
    mainArea
    + booStatue
    + chucklehuck
    + castleTown
    + startingFlag
    + chuckolatorFlag
    + piranhaFlag
    + kidnappedFlag
    + beanstarFlag
    + birdoFlag
    + winkle
    + sewers
    + hooniversity
    + surfable
    + airport
    + gwarharEntrance
    + teeheeValley
    + fungitown
    + fungitownBeanstar
    + fungitownBirdo
    + bowsers
    + bowsersMini
    + jokesEntrance
    + jokesMain
    + postJokes
    + theater
    + oasis
    + gwarharMain
    + baseUltraRocks
    + coins
    + specialCoins
)

location_table: typing.Dict[str, int] = {location.name: location.id for location in all_locations}
