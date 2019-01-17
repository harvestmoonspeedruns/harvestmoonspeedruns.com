import os
import json

def main():
    with open("_data/games.json") as file:
        for game in json.load(file).values():
            basedir = os.path.join("wiki", game["abbr"])
            if not os.path.exists(basedir):
                os.makedirs(basedir)
            if not (os.path.exists(os.path.join(basedir, "index.md")) or os.path.exists(os.path.join(basedir, "index.html"))):
                with open("bin/_templates/game_index_template.md") as to_copy:
                    s = to_copy.read()
                    s = s.replace("[TITLE]", game["name"])
                    s = s.replace("[ABBR]", game["abbr"])
                    with open(os.path.join(basedir, 'index.md'), "w") as to_write:
                        to_write.write(s)

            for category in game["categories"]:
                directory = os.path.join(basedir, category["abbr"])
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    open(os.path.join(directory, '.gitkeep'), 'a').close()

if __name__ == "__main__":
    main()