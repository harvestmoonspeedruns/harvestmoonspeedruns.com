---
type: "game"
layout: "git-wiki-default"
title: "Doraemon Story of Seasons: Friends of The Great Kingdom"
abbr: "doraemon_story_of_seasons_friends_of_the_great_kingdom"
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
