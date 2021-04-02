---
type: "guide"
category: "marriage"
game: "hmawl"
layout: hm-wiki-guide
version: 0.1.0
---

# Muffy

## Memory Addresses 

Some data on this page was obtained by using [Dolphin Memory Engine](https://github.com/aldelaro5/Dolphin-memory-engine/releases) to find, read, and modify memory addresses. You can watch the contents of these addresses by opening this file in Dophin Memory Engine while Dolphin is running, or in a text editor (since it is formatted as JSON):

- [.dmw file](/wiki/hmawl/hmawl-gc-ntsc-u.dmw) (GameCube, NTSC-U)

## Route

- RNG Gotchas
	- Muffy must be indoors to earn conversation points on SP 1 and SP 2. ~50% success.
	- Muffy must be in town to trigger the third heart event on SU 1. ~20% success.

#### Current Fastest Route

- SP 1, 11a
	- initial +18
	- eject record
	- milk cow, keep 2
	- pick 3 flowers
	- indoor gifts +10
	- trigger Eek +5 = 33
- SP 2, 12:30p
	- indoor gifts +8 = 41
- SP 3 through 9
	- sleep
- SP 10, 1:15p
	- trigger Clumsy +10
	- indoor conversations +5 = 56
- SU 1, 2p
	- early blue feather
	- Interaction Bonus +10
	- trigger Friend’s Wedding +10
	- get blue feather from shelf
	- milk cow, keep 1
	- outdoor gifts +4 = 80
	- propose

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

## Heart Points (Muffy)

Muffy begins Spring 1 with 18 points (see [Jealousy Penalty](#jealousy-penalty)).

### Gifts

Points | Category | Note
---: | --- | ---
+3 | Loved Item | Amorous flower, any coin, Moon Ore, Temple Ore, Propser Ore, Breeze record, Summer Memories record, Golden wool
+3 | Always Loved Item | Big Huchep, any butter, any cheese
+2 | Flower | Any flower besides Amorous (Toy Flower, Mist Moon, Trick Blue, Goddess drop, Happy Lamp, Gemsoil, Upseed). Select the first option, "Yes". Only +1 for "If you want it."
+1 | Milk | any milk
0 | Other Categories | any crop, any seed, any egg, any other prepared food, all other fish, all other records, all other ores, Ruby Spice, Gold medal, necklace, sheet music, tumtum (drum), surprising item (fireworks), nice item (white wool), hated items (Big Sharshark, Big Colombo, Colombo, failed cooking, soups?), dirty items (all fossils, all tools, fertilizer, fodder, good fodder), trash (all other digsite artifacts), all wild weeds and mushrooms (mugwort, royal fern, bracken, sorrel, hackberry, trumpet (mushroom), Matsutake (mushroom))
N/A | no response | all toys, all potions, birdseed, animal medicine, (regular) wool

### Conversation
Points | Category | Note
---: | --- | ---
+1 | Greeting | Not awarded the first time you talk to her.
+2 | Question 1 | Only available indoors. Earned by selecting "I wanted to see you", the first option. Zero for "Wanted to talk", and -1 for "Nothing in particular".
+2 | Question 2 | Only available indoors. Earned by selecting "Just to see you", the second option. Zero for "I wanted to talk", and -1 for "I have a funny joke".
0 | Other | "I think a man who works hard is sexy, though", or "Are you here to see me or Griffin?"

### Heart Events

Each of Muffy's events seems to require that all previous ones occur first, and on separate days. Sunny daytime is seemingly not necessary.

Points | Requirement | Trigger | Description | Best Choices | You Warp To | She Warps To
---: | ---: | --- | --- | --- | --- | ---
+5 | 20+ points | Exit your house when Muffy is awake. | Eek | Default choices (-5 for "What did you want?") | In front of barn | Near bridge (E 170, N 155), heading toward previous location
+10 | 40+ points | Enter the bar after 11am on a bar day. | Clumsy | Default choice (-10 for "Go back together") | Inside bar | Inside bar
+10 | 60+ points | Exit your house when she is in town (standing still >300 E). Typically 1:45pm-4pm on a town day. | Friend's Wedding | Alt choice, "Forget Valley" (only +5 for "Town") | Farm entrance (E 166, N 150) | Exiting the bar (E 88, N 139.25)
+10 | 80+ points | Go to sleep between 6pm and 11pm | Strange Man | Default choice (-10 for "I'll walk you home") | Sleeping | Sleeping

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

Unique to Muffy, but Celia has a similar penalty. You lose part of the inital 18 point bonus if you interact enough times with a group of townsfolk.

- -10 points if you have >15 interactions with members of only one group.
- -18 (total) if you have >15 interactions with neighbors and >15 interactions with young women. 
	- Neigbors: Grant, Wally, Kate, Chris
	- Young women: Celia, Nami, Flora, Chris

#### Lifetime Interactions

Unique to Muffy: if you have interacted with her enough times, you activate a +10 point bonus. The number of required lifetime interactions depends on the month and day, and the bonus will deactivate on days when the requirement is not met.

- Required interactions:
	- Spring: 5 × [day of the month]
	- Summer: 10 × [day of the month]
	- Fall (unconfirmed): 15 × [day of the month]
	- Winter (unconfirmed): 20 × [day of the month]
- For example, 100 lifetime interactions are needed to have the bonus on Summer 10, but only 15 on the next day, Fall 1.

Each day you can earn up to 5 interactions. (Doing more than that isn't counted.) Since there is no glitchless way to interact with Muffy before she wakes up on Spring 1, it is impossible to catch up to the required number during Spring.

## Schedule

(This [Map](/assets/images/map.jpg) helps to locate in-game coordinates.)

Muffy wakes up at 10am.

- Bar Day
	- starts working 1pm, can’t visit or gifts
	- goes to bed at 00:36am
- Town Day
	- mostly incompatible with rain
	- may leave bar ~11:30
	- may stop and chat in the hotel lobby ~noon-12:30p
	- she will typically be in town between 1:45p and 4p
	- then stop at Vesta’s farm, northwest riverbank at ~8:15p, southeast riverbank at ~9:15p and ~9:55, then home at ~11:30p
- Outdoor Day
	- mostly incompatible with rain
	- northwest riverbank 5:??p
	- Carter’s tent ~8:20p
	- southeast riverbank ~10:50p
	- northwest riverbank ~0:20a (passes my farm ~0:50a)
	- home at 1:30a, goes to bed as soon as she reaches the ladder

Probabilities have not been measured, but Town Day seems more common on odd-numbered days. Town Day and Outdoor Day both seem more common on Spring 3 and Spring 7, and less common on rainy days.


## Old Route

*NOTE: THIS IS A PREVIOUS RECORD-SETTING ROUTE. IT FEELS LIKE IT WORKS 50% OF THE TIME.*

1. Once introduction is complete sleep once to put the time at 11am
1. Let the cow out of the bar and milk it. It will be 2 Milk B.
1. Go pick up 3 Toy Flowers around gravestone hill
1. Meet Muffy in back room and give her a flower (Select 2nd option), milk, and talk to her until she asks a question. Response is "[...] to see you [...]"
1. Go back home and sleep 4 times
1. Take Breeze off record player in house
1. Wait to leave house until 12:30pm
1. First Heart Event should trigger, Select 1st option each time.
1. Meet Murphy walking near the front of your farm. Give Flower (Don't forget 2nd option), Milk, Breeze Record
1. Pick up 2 more Toy Flowers
1. Enter the Mine and collect 3 items (Gold Coin or Moon Ore)
1. Head to farm, on the way grab mogwart next to river and eat.
1. Milk Cow, grab 3 of the 4 Milk A
1. Sleep 3 times
1. Go to back of bar and give flower, talk, milk, and mining item (Gold Coin or Moon Ore)
1. Go back to house and sleep 4 times
1. Head back to bar and pull flower out before entering outside door. Enter at 11am
1. Second Heart Event: Select 1st option each time.
1. Once in bar quickly give gift in hand. Hopefully you can give at least 1 gift and talk to her in the front of bar
1. Follow her into the back room and give remaining gifts flower, talk, milk, mining item
1. Go back home and wait until noon to sleep.
1. Sleep to Summer 1 (Blue Feather Event)
1. Go to tool storage shed and grab Blue Feather out.
1. Go to bar and give Muffy the flower, talk, milk, and mining item.
1. Lastly give her the Blue Feather.
