---
type: "game"
layout: "git-wiki-default"
title: "Harvest Moon: Save the Homeland"
abbr: "hmsth"
---

{% assign game = site.data.games[page.abbr] %}

# {{page.title}}
[speedrun.com]({{game.url}})

## Categories

<table class="category-table">
    {% for category in game.categories %}
    <tr>
        <th><a href="/wiki/{{game.abbr}}/{{category.abbr}}">{{ category.name }}</a></th>
        {% for subcategory in category.subcategories %}
        <td><a href="/wiki/{{game.abbr}}/{{category.abbr}}/{{subcategory.abbr}}">{{ subcategory.name }}</a></td>
        {% endfor %}
    </tr>
    {% endfor %}
</table>

## StH Basics
[Affection](basics/affection.md)

[Cutscenes by ending](basics/cutscenes.md)

Glitches and exploits

Villager schedules

Gift charts
