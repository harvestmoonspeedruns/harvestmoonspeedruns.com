# Items and Locations

## Map Locations

See the [Map](/assets/images/map.jpg) for reference.

Location                   | N          | E          | Nf     | Ef
:--- | ---: | ---: | ---: | ---:
Door to player's house     | 0x43280000 | 0x42f20000 | 168.00 | 121.00
Return from Mineral Town   | 0x43164c00 | 0x437ebe00 | 150.29 | 254.74
Beach tip                  | 0x42334060 | 0x4301fb2c |  44.81 | 129.98
Northwest tip, Villa area  | 0x436f14a4 | 0x41d73ae1 | 239.08 |  26.90
Northeast tip, Villa area  | 0x436f14a4 | 0x4280ca34 | 239.08 |  64.39
Springs, north tip         | 0x43911a3b | 0x42ebf399 | 290.20 | 117.97
Waterfall                  | 0x43907906 | 0x434c481b | 288.94 | 204.28
Artist's property, SE tip  |            |            |  67.50 |  48.03
Large plot (10 by 14), below | | | | 
NW                     | 0x43631503 | 0x42e441ab | 227.08 | 114.12
NE                     | 0x43630e2c | 0x42ffd50b | 227.05 | 127.91
SW                     | 0x435906cf | 0x42e42a92 | 217.02 | 114.08
SE                     | 0x43590e27 | 0x430011fe | 217.05 | 128.07

## Room numbers
```
1 Outside

3 Home living room

7 Barn

10 Player storeroom

12 Shed
13 Takakura's house
14 Pyro brothers' loft
15 Cody's studio
16 Laboratory
17 Yurt
18 Bar
19 Bar bedroom
20 Hotel lobby
21 Hotel bedroom
22 Hotel kitchen
23 Hotel upstairs left room
24 Hotel upstairs right room
25 Hotel upstairs hallway

20 Inn Entrance

22 Inn Kitchen

25 Inn Upstairs

27 Villa Romana's bedroom
28 Villa Sebastian's bedroom
29 Villa kitchen
30 Villa upstairs tea room
31 Villa entryway
32 Villa upstairs hallway
33 Wally's house (West town house) downstairs
34 Wally's house (West town house) upstairs

37 Nina's house (East town house)

39 Carter's tent
40 Digsite
41 Sprite tree interior
42 Vesta's storeroom
43 Vesta's downstairs
44 Vesta's upstairs
```

## Person current room (8109E1XX)

(ID is this minus 0x10 divided by 4)
```
10 Player
14 (future kid?)
18 Celia
1c Muffy
20 Nami
24 Murrey
28 Carter?
2c Takakura
30 Romana
34 Lumina
38 Sebastian
3c Wally
40 Chris
44 Hugh
48 (future?)
4c (future?)
50 (future?)
54 Galen
58 Nina
5c Daryl
60 Gustafa
64 Cody
68 Kassey
6c Patrick
70 Tim
74 Ruby
78 Rock
7c Griffin
80 Flora (Carter's assistant)
84 Vesta
88 Marlin
8c Doctor Hardy
90 Nic
94 Nak
98 Flak
9c
a0 Van
a4
a8
ac
b0
b4 Orange cat (Romana's)
b8 White cat (Romana's)
bc
```

## Person coordinate addresses
```
North = (ID * 0x0c) + 8109daf8
East = North + 8
```

## Item numbers
```
1 0x1 Fertilizer
2 0x2 Birdseed
3 0x3 Fodder
4 0x4 Good Fodder
5 0x5 Animal Medicine
6 0x6 Mothers Milk
7 0x7 Normal Milk C
8 0x8 Normal Milk B
9 0x9 Normal Milk A
10 0xA Normal Milk S

15 0xF Star Milk-C

20 0x14 Brown Milk-B
21 0x15 Brown Milk-A
22 0x16 Brown Milk-S
23 0x17 Goat Milk
24 0x18 Good Goat Milk
25 0x19 Wool
26 0x1A White Wool
27 0x1B Golden Wool
28 0x1C Egg
29 0x1D Golden Egg
30 0x1E Fertilized Egg
31 0x1F Tomato-B
32 0x20 Tomato-A
33 0x21 Tomato-S
34 0x22 Watermelon-B
35 0x23 Watermelon-A
36 0x24 Watermelon-S
37 0x25 Strawberry-B
38 0x26 Strawberry-A
39 0x27 Strawberry-S
40 0x28 Melon-B
41 0x29
42 0x2A
43 0x2B Turnip-B
44 0x2C Turnip-A
45 0x2D Turnip-S
46 0x2E Potato-B
47 0x2F Potato-A
48 0x30 Potato-S
49 0x31 Carrot-B
50 0x32 Carrot-A
51 0x33 Carrot-S
52 0x34 Sweet Potato-B
53 0x35 Sweet Potato-A
54 0x36 Sweet Potato-S
55 0x37 Gretoma-B

100 0x64 Yamato-B

150 0x96 Layer4-S

200 0xC8 [nothing]

250 0xFA Phuju-B

300 0x12C Watermelon Seed-A*
400 0x190 Berrytoma Seed-S*
500 0x1F4 Bashota Seed-B*
600 0x258 Cabber Seed-A*
700 0x2BC Camelo Seed-S*
800 0x320 Layer8 Seed-B*
900 0x384 Layer17 Seed-A*
1000 0x3E8 Layer25 Seed-S*
1074 0x432 Layer9 Seed-S
1075 0x433 Mugwort
1076 0x434 Royal Fern
1077 0x435 Bracken
1078 0x436 Sorrel
1079 0x437  Hackberry
1080 0x438 Trumpet (mushroom)
1081 0x439 Matsutake (mushroom)
1082 0x43A Toy Flower
1083 0x43B Mist Moon
1084 0x43C Trick Blue
1085 0x43D Amorous (flower)
1086 0x43E Goddess Drop
1087 0x43F Happy Lamp
1088 0x440 Gemsoil
1089 0x441 Upseed (flower)
1090 0x442 Coin
1091 0x443 Silver Coin
1092 0x444 Gold Coin
1093 0x445 Skull Fossil
1094 0x446 Fossil
1095 0x447 Hip Fossil
1096 0x448 Strange Fossil
1097 0x449 Back Fossil
1098 0x44A Tablet C
1099 0x44B Tablet D
1100 0x44C Tablet E
1101 0x44D Tablet F
1102 0x44E Tablet G
1103 0x44F Human Statue
1104 0x450 Horse Statue
1105 0x451 Jade Ball
1106 0x452 Strange Item
1107 0x453 Stone Disc
1108 0x454 Moon Ore
1109 0x455 Sugar Ore
1110 0x456 Hop Ore
1111 0x457 Temple Ore
1112 0x458 Prosper Ore
1113 0x459 Ball
1114 0x45A Blocks
1115 0x45B [nothing]
1116 0x45C [nothing]
1117 0x45D [nothing]
1118 0x45E Closed Book 1
1119 0x45F [nothing]
1120 0x460 Closed Book 2
1121 0x461 [nothing]
1122 0x462 Closed Book 3
1123 0x463 [nothing]
1124 0x464 Closed Book 4
1125 0x465 [nothing]
1126 0x466 Scratch Pad
1127 0x467 [nothing]
1128 0x468 Car (toy)
1129 0x469 Ruby Spice
1130 0x46A Tumtum (drum)
1131 0x46B Gold Medal
1132 0x46C Necklace
1133 0x46D Music Sheet
1134 0x46E Fireworks
1135 0x46F Big Nyamame
1136 0x470 Nyamame
1137 0x471 Big Huchep
1138 0x472 Huchep
1139 0x473 Big Yamame
1140 0x474 Yamame
1141 0x475 Big Snelt
1142 0x476 Snelt
1143 0x477 Big Arna
1144 0x478 Arna
1145 0x479 Big Rainbob
1146 0x47A Rainbob
1147 0x47B Big Sharshark
1148 0x47C Sharshark
1149 0x47D Big Colombo
1150 0x47E Colombo
1151 0x47F Failed cooking

1156 0x484 Light Pickles (turnip only)

1160 0x488 Curry

1163 0x48B Stew

1175 0x497 Mixed Veggies

1178 0x49A Veggie Pasta

1181 0x49D Gratin

1200 0x4B0 Adult Salad

1206 0x4B6 Fruit Salad

1218 0x4C2 Red-Hot Pie

1225 0x4C9 Good4U Soup

1230 0x4CE Dhibe Cake

1235 0x4D3 Juice DX

1240 0x4D8 Tropical Punch

1245 0x4DD Sour Cocktail
1246 0x4DE Heavy Hoe
1247 0x4DF Hoe
1248 0x4E0 Light Hoe
1249 0x4E1 Strange Hoe
1250 0x4E2 Weird Hoe
1251 0x4E3 Hoe
1252 0x4E4 Light Hoe
1253 0x4E5 Heavy Sickle
1254 0x4E6 Sickle
1255 0x4E7 Light Sickle
1256 0x4E8 Strange Sickle
1257 0x4E9 Weird Sickle
1258 0x4EA Sickle
1259 0x4EB Light Sickle
1260 0x4EC Watering Can S
1261 0x4ED Watering Can
1262 0x4EE Watering Can L
1263 0x4EF Watering Can W
1264 0x4F0 Watering Can
1265 0x4F1 Watering Can L
1266 0x4F2 Fishing Pole
1267 0x4F3 Fishing Pole G
1268 0x4F4 [nothing]
1269 0x4F5 [nothing]
1270 0x4F6 Milker
1271 0x4F7 Milker
1272 0x4F8 Goat Milker
1273 0x4F9 Goat Milker
1274 0x4FA Wool Shears
1275 0x4FB Wool Clippers
1276 0x4FC Electric Clippers
1277 0x4FD Electric Clippers
1278 0x4FE Brush
1279 0x4FF [nothing]
1280 0x500 [nothing]
1281 0x501 [nothing]
1282 0x502 [nothing]
1283 0x503 [nothing]
1284 0x504 Cheap Butter
1285 0x505 Regular Butter
1286 0x506 Good Butter
1287 0x507 Moms Butter
1288 0x508 Goat Butter
1289 0x509 Good Goat Butter
1290 0x50A Cheap Cheese
1291 0x50B Regular Cheese
1292 0x50C Good Cheese
1293 0x50D Moms Cheese
1294 0x50E Goat Cheese
1295 0x50F Good Goat Cheese
1296 0x510 Spring Song
1297 0x511 Town Spirit
1298 0x512 Flower Bud Fall
1299 0x513 64 Memories
1300 0x514 Marin Jazz
1301 0x515 Butterfly
1302 0x516 Summer Memories
1303 0x517 Joy of Fall
1304 0x518 Winter HM
1305 0x519 The Bride
1306 0x51A Breeze (in record player)
1307 0x51B Quiet Winter (on shelf)
1308 0x51C [Record13 empty]
1309 0x51D [Record14 empty]
1310 0x51E [Record15 empty]
1311 0x51F Blue Feather
1312 0x520 Turbojolt (red)
1313 0x521 Bodijizer (purple)
1314 0x522 Bodihyper (green)
1315 0x523 [nothing]
1316 0x524 [nothing]
1317 0x525 [nothing]
1318 0x526 [nothing]
1319 0x527 [nothing]
1320 0x528 [nothing]

1325 0x52D [nothing]

1350 0x546 [nothing]

1375 0x55F [nothing]

1400 0x578 [Invalid pointer]

1500 0x5DC [nothing]
```
