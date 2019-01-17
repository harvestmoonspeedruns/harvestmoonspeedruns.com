import json
import collections

import srcomapi, srcomapi.datatypes as dt
api = srcomapi.SpeedrunCom(); api.debug = 0

def buildSlug(name):
    return name.lower().replace("%", "_").replace(" ", "-")

def buildSubcategory(subcategory):
    return {
        "abbr": buildSlug(subcategory["label"]),
        "name": subcategory["label"],
        "rules": subcategory["rules"]
    }

def buildCategory(category):
    subcat = next((var for var in category.variables if var.is_subcategory), None)

    return {
        "abbr": buildSlug(category.name),
        "name": category.name,
        "rules": category.rules,
        "subcategories": not subcat or [buildSubcategory(values) for values in subcat.values["values"].values()]
    }

def buildMiscSubcategory(category):
    return {
        "abbr": buildSlug(category.name),
        "name": category.name,
        "rules": category.rules,
    }

def buildMisc(categories):
    if len(categories) <= 0: return []

    return [{
        "abbr": "miscellaneous",
        "name": "Miscellaneous",
        "rules": "",
        "subcategories": [buildMiscSubcategory(category) for category in categories]
    }]

def main():
    games = [dt.Game(api, game) for game in api.get('series/049rd64v/games')]

    gamesData = {}

    for game in games:
        miscCategories = []

        gamesData[game.abbreviation] = {
            "name": game.name,
            "boxart": game.assets["cover-large"]["uri"],
            "url": game.weblink,
            "abbr": game.abbreviation,
            "categories": [buildCategory(category) for category in game.categories if not category.miscellaneous] + buildMisc([category for category in game.categories if category.miscellaneous])
        }

    with open('_data/games.json', 'w') as file:
        json.dump(gamesData, file)


if __name__ == "__main__":
    main()
