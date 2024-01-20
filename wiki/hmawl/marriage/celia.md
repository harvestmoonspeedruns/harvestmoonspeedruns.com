---
type: "guide"
category: "marriage"
game: "hmawl"
layout: hm-wiki-guide
version: 0.1.0
---

# Celia

#### Memory Addresses 

Some data on this page was obtained by using [Dolphin Memory Engine](https://github.com/aldelaro5/Dolphin-memory-engine/releases) to find, read, and modify memory addresses. You can watch the contents of these addresses by opening this file in Dophin Memory Engine while Dolphin is running, or in a text editor (since it is formatted as JSON):

- [.dmw file](/wiki/hmawl/hmawl-gc-ntsc-u.dmw) (GameCube, NTSC-U)

Refer to [Items and Locations](/wiki/hmawl/items-and-locations) for their specific memory values.

## Route

- RNG gotchas
	- On SP 8, Celia needs to be downstairs with Vesta and Marlin. See Arranged Marriage in [heart events](#heart-events) for more details.
		- 25-50% success rate
		- Non-recoverable
	- On SP 5 and 6, Celia may be indoors, enabling you to earn the anecdote point. If you miss it both days, recover with three chicken nuzzles.
		- 55% success rate
		- Recoverable
	- The chicken may randomly sleep, preventing you from raising its happiness. If it happens on SP 4, 5, 6, or 8, just come back later in the day. If it happens on SP 2, 3, or 7 you will need to make up for the loss using extra nuzzles or anecdote points.
		- Recoverable

#### Points breakdown
- Total: 80 points
	- 10 default
	- 20 from heart events
	- 7 from animal happiness
		- 250 happ per day for seven days, with five nuzzles and two days ignored
	- 43 from seven visits (gifts & conversation)
		- +4, chicken warp, 11:59
		- +7, before Shopping, >1p, (Schedule 1: < 2p), (Schedule 2: < 3p)
		- +6, SP 05
		- +6, SP 06
		- +6, after Don’t Move
		- +7, before Arranged Marriage
		- +7, before proposal

#### Current Fastest Route

- SP 1 = 10
	- Order chicken
- SP 2, ~11:07
	- Get mugwort
	- Let out cow (cow will occasionally die late in the run if you keep it inside)
	- Go to farm
		- Eat mugwort
		- 6 flowers (4 or 5 if you don't have time, pick up remaining at goddess pond on day 7)
		- Gifts +4 (don't change rooms after giving gifts)
		- Noon, chicken warp home 1p
	- 350 happ
- SP 3
	- Nuzzle
	- Get extra egg
	- 700 happ
- SP 4, ~1:11p = 16
	- Nuzzle
	- Go to farm
		- Gifts +7
		- Trigger heart event Shopping +5
		- Go home
	- 950 happ
- SP 5, ~2:00p = 29
	- Optional nuzzle SP 5
	- If she’s inside on SP 5 or 6, you can theoretically stop nuzzling because of the anecdote point. Normally you need to nuzzle on SP 6, 7, and 8.
	- Go to farm
		- Gifts +6 (or +7 and save three nuzzles)
		- Go home
	- 1200 happ
- SP 6
	- See above about nuzzles
	- Go to farm
		- Gifts +6 (or +7 and save three nuzzles)
		- Go home
	- 1550 happ
- SP 7, ~10:29 = 43
	- Trigger heart event Don’t Move +5
		- regardless of time, C warps to (167,228)
		- Pick up toy flower (you should have one flower in hand and 2 in inventory at this point, pick up 1 or 2 additional if you didn't get them on day 2)
		- Gifts +6
		- Go home
	- 1900 happ
- SP 8, ~11:10 = 55
	- Look for Van (to skip the cutscene if needed)
	- Go to farm
		- Gifts +7
		- Trigger heart event Arranged Marriage +10
			- regardless of time, C warps to (171,147)
		- Go home
	- 2250 happ
- SP 9-10 = 73
	- Sleep
	- 2110 happ
- SU 1, ~6:10a = 73
	- Wake up 12a-5a?, blue feather cutscene
	- Get blue feather from shelf
	- Look for Van
	- Go to farm
		- Gifts +7
		- Propose


## Heart Points (All Bachelorettes)

- Each bachelorette has up to 100 heart points, 20 per heart.
	- One red heart is 20-39 points
	- Two is 40-59
	- Three is 60-79
	- Four is 80+
- Having 80+ points is the only requirement for proposing successfully.
	- Proposing below 80 doesn’t incur a penalty the first time, but subsequent sub-80 proposals are -10 each.
	- Points are not affected by proposing to other bachelorettes. (Nor, seemingly, any interaction with other people.)

- Every day she can accept one gift or conversation in each category.
	- All categories reset when she wakes up.

## Heart Points (Celia)
Celia begins Spring 1 with 10 points (see [Jealousy Penalty](#jealousy-penalty)).

### Gifts

Points | Category | Note
---: | --- | ---
+3 | Loved Item | (any wild flower, Moon Ore, music record, statue)
+2 | Egg | (Egg, Golden Egg)
+2 | Dish | (any prepared food)
+2 | Crop | (any crop)
won't accept | Other | milk, cheese, butter, fertilizer, seeds, mugwort, potion, tools, wool, coins, fish, fossils, tablets, jade ball,  strange item, stone disc, other ores, toys, books, Ruby Spice, Tumtum (drum), Gold Medal, necklace, sheet music, fireworks

### Conversation

Points | Category | Note
---: | --- | ---
+1 | Greeting | (Not awarded the first time you talk to her.)
+1 | Anecdote | (Only available indoors. Earned after either "Vesta's vegetables are great, you know." or "My room is the loft, but I like it.")

### Heart Events
All of Celia's events require sunny daytime.

Points | Requirement | Trigger | Description | Best Choices | You Warp To | She Warps To
---: | ---: | --- | --- | --- | --- | ---
+3 | None | Exit Vesta’s house when Celia is outdoors | Plant Power | Alt choice, then default choice | Stay put | Town (90, 150)
+5 | 20+ points | Enter Vesta’s house when Celia is downstairs and the others are in the storeroom. | Shopping | Default choices | Stay put | Off-map
+5 | 40+ points | Exit your house | Don't Move | Default choices | Springs | Path to Springs (228,167)
+10 | 60+ points | Enter Vesta’s house when Celia is downstairs and has been in the same room as Vesta and Marlin since passing 60 points. (They need to have "discussed" it.) | Arranged Marriage | Alt choice, then default choices | Springs | Bridge (171,147)

### Bonus Points

Bonus points are heart points which are re-calculated when she wakes up every morning.

#### Farm Work

Common to Celia and Muffy: you earn bonus points from the work of doing chores. Each 100 work corresponds to +1 bonus point.

- Work amounts
	- 1 per square watered/hoed or grass cut
	- 3 per seed planted
	- 3 per fodder put in a trough
		- none for simply taking it out of the silo
	- 7 for filling any water can (takes 3 seconds)
	- 9 for milking a cow
		- 4 for failed milking
		- none for talking or nuzzling

#### Jealousy Penalty

Unique to Celia, but Muffy has a similar penalty. You lose the initial 10 point bonus if you interact enough times with other young women.

- -10 points if the other young women > 15 combined interactions
	- includes Muffy, Nami, Flora, Chris

#### Hugh Friendship

Unique to Celia: you earn points from befriending Hugh. Each gift to Hugh converts to +1 heart point when Celia wakes up. (-1 for being anywhere below 17 friendship. The default is 50 friendship.)

- Gifts to Hugh
	- +1 favorite item (up to 3 per day)
		- any milk
		- maybe others?
	- +1 "so good" item (up to 3 per day)
		- any coin
		- any wool
		- Moon ore (not sugar ore)
		- ball
		- blocks
		- maybe others?
	- doesn't accept any egg
	- doesn't accept tomato, or probably any vegetable
	- doesn't accept goddess drop, or probably any flower
	- doesn't accept fodder
	
#### Animal Happiness

Unique to Celia: you earn bonus points from the happiness of your animals.

- +10 is earned for the cow’s initial happiness of 1000. (Dropping to 999 or less loses all 10.)
- +1 is earned for each multiple of happiness of the happiest animal only.
	- For a chicken, each 300.
	- For a cow, each 30 above the default 1000.
- Points are lost if happiness drops below the levels where they were earned.

A heart emote from the animal indicates that happiness has increased. Happiness cannot drop below zero. Since the happiness of a cow or chicken is virtually unlimited (32-bit signed integer), this is an attractive place to look for glitches.

##### Cow Actions

Happiness | Action | Cooldown
---: | --- | ---
10 | Talk | Around 5:30 am?
15 | Nuzzle | One game-hour?
0 | Ignored for the day | N/A
-20 | Show Dog | Instant

##### Chicken Actions

Happiness | Action | Cooldown
---: | --- | ---
250 | Put Down | Around 5:30 am
100 | Nuzzle | One game-hour
-50 | Unwanted nuzzle (when sleeping, or 4th and 5th times without waiting for cooldown) | Instant
-50 | Show Dog | Instant
-70 | Ignored for the day | N/A

## Schedule

(This [Map](/assets/images/map.jpg) helps to locate in-game coordinates.)

Here are Celia's standard paths:

- Schedule 0
	- C upstairs all day
- Schedule 1
	- C outside 7:45-9:45
	- C downstairs 10-2p 
	- C upstairs 2p-6p
	- C downstairs 6p-8p
- Schedule 2
	- C outside 7:30-11
	- C downstairs 11-3p
	- C outside 3-5:30
	- C downstairs 5:30-8
- Schedule 3
	- C outside 7:30am-9am
	- C off-farm 9a-8:30p (may be earlier by ~45min)
		- northwest riverbank 11
		- southwest riverbank 12
		- mid-trail 1:30
		- around spring 3:15-4:30
	- C downstairs 8:30-9
- Schedule 4
	- off-map ?-2p? -11a?
	- walking home 2?-3?
	- downstairs 3? 11?-3:15
	- off-farm 3:15->10p
		- Romana’s Villa

And here is the estimated probability of which path she'll take on particular days:

- normal day
	- 50% upstairs all day
	- 5% upstairs pm from rain (not on SP 08)
	- 45% outside all day
- SP 3 and 7 - Schedule 0, Schedule 3, or Schedule 4
	- 40% upstairs all day
	- 40% hike to springs
	- 20% go to Mineral Town
- SP 9
	- 25% upstairs all day
	- 25% upstairs pm from rain
	- 50% outside all day
- SP 10 and SU 1
	- 30% upstairs all day
	- 55% upstairs pm from rain
	- 15% outside all day 
