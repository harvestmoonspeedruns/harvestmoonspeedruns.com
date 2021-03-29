---
type: "guide"
category: "marriage"
game: "hmawl"
layout: hm-wiki-guide
version: 0.1.0
---

**Heads up:** This page assumes you have some experience **routing** HM:AWL. It is incomplete, and not a good place to start running the game.

## Why is this Nami guide incomplete?

The route outlined below is hypothetical. It depends on major RNG manipulation.

Nami (or Gustafa/Cody/Patrick) would need to be in a good location nearly every day from Spring 1 to Summer 1. Currently I don't know of a practical way to do this. If a method were discovered, we could cut the current WR in half, down to about 25:52. Small improvements over the current WR are also possible. But cutting it in half would be so much more impressive!

The game appears to be input-deterministic, so a TAS could do it. Once the first TAS solution is found, someone could write scripts in Dolphin-Lua to try and brute-force a "sweet spot" for human runners to aim for.

(Other suggestions welcome!)

## Hypothetical route

- SP 1
	- Get record
	- Let out cow
	- conversation and vinyl record +6 = 6
- (at some point trigger Get To Work +10)
- SP 2 through 10 (+38 = 54)
	- avg convo and interactions +4
	- (need an extra +2 somewhere)
	- (default 5.82 friend interactions per point)
- SU 1
	- late blue feather
	- get second vinyl record
	- trigger Forgot To Pay +20
	- conversation and record +6 = 80
	- propose

## Conversation
- +2 second interaction in bar
- +2 "Not that there's anything wrong with that", in hotel
- +2 second interaction, often "I can't believe I stayed here the whole year", outdoors, yurt, Vesta's storehouse

## Bonus Points
- Interactions and friendship with Gustafa, Cody, and Patrick
	- Friendships get added together and must be 150 to 209
		- default is 165
	- Interactions get added together and converts at 6.4 per point at 150, 5.82 at 165, and down to 4.6 per point at 209.

## Gifts
- Loved Item +2
	- Trick Blue, Gemsoil
	- Silver Coin
	- Skull Fossil (can be dug up in year 1)
	- Human Statue (can be dug up in year 1)
	- Horse Statue
	- Sugar Ore, Hop Ore
	- all records
- Favorite Food +2
	- Curry, Stew, Veggie Pasta, Gratin, Red-Hot Pie
- No other item in the game gives any points.

## Heart Events

- Get To Work @20
	- default
		- -10
	- alt
		- +10
		- 53 sec
		- she warps to N 154, E 168
			- possible she walks toward wherever she was previously
		- you warp to N 205, E 129
- Forgot to Pay @40 (Muffy and Nami are both in bar main area)
	- Can I sit here?
		- Ask why Nami's here
			- Nod in Nami's direction +5
				- I'll pay
					- (lose 256 G)
				- Ha ha ha
					- (no effect)
			- Hmm…
				- (same as Tell why I'm here)
		- Tell why I'm here
			- Sure +5
			- Not really +5
			- I don't keep track +20
				- +20
				- 40 sec
				- She warps to exiting the hotel
				- You warp to exiting the bar
	- Let's drink together
		- (ends)
- She's Gone @60 (be inside my house when 8am strikes)
	- Okay
		- (zero)
	- I'll look for her
		- +5
		- 96 sec
		- time warps to 11am
		- she warps to exiting hotel
		- you warp to front of hotel
- Find a Job @80 (Nami is in her room but not asleep)
	- Sure
		- +10
		- 40 sec
		- she warps to her room
		- you warp to exiting hotel
	- Not a good idea
		- -10

## Time cost per point

- convenient interactions with friends
	- 11.6s/pt Cody, Gustafa (doesn't include travel time)
		- 0.86 pts takes 10s
- 16s/pt Wake up conversation
	- 4 pts takes 55s, 0:36g
- 19s/pt Bar conversation
	- 4 pts takes 75s, 0:60g
- 35s/pt Digging
	- 270s to get 4 gifts (8 pts)
	- about 4 s per gift giving animation

- Total time estimate = 335+300+4+73+10+93+15+768 = 1598s (goal is 1552s, half of current record)
	- intro = 335s (JP version)
	- all sleeps = 300s
		- 7.5s x (4 x 10 (would be 41, but activities will burn at least 8 game hours I think))
	- get first vinyl record = 4s?
	- blue feather event = 73s?
	- get blue feather and second vinyl record = 10s?
	- heart events = 93s
		- 53s, Get to Work
		- 40s, Forgot to Pay
	- proposal event = 15s?
	- 9 trips = 768s
		- 192s, 3 wakeups
		- 456s, 6 bar trips
		- 120s, 12 friend encounters

## Schedule
- TODO
	- map the sweet spots I can hit on SP 1 when Nami is walking into or out of bar/hotel
	- start making a probability chain of hitting more sweet spots on later days
	- after finding a complete chain for Nami, start on her friends