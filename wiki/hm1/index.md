---
type: "game"
layout: "git-wiki-default"
title: "Harvest Moon"
abbr: "hm1"
---

{% assign game = site.data.games[page.abbr] %}

# {{page.title}}
[speedrun.com]({{game.url}})

<div class="float-right"><img src="{{game.boxart}}" alt="{{game.name}} Cover Photo" /></div>
<div class="clear"></div>
## Categories

<table class="category-table">
    {% for category in game.categories %}
    <tr>
        <th><a href="/wiki/{{category.abbr}}">{{ category.name }}</a></th>
        {% for subcategory in category.subcategories %}
        <td><a href="/wiki/{{category.abbr}}/{{subcategory.abbr}}">{{ subcategory.name }}</a></td>
        {% endfor %}
    </tr>
    {% endfor %}
</table>
