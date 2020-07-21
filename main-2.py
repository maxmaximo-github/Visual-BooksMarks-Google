#!/usr/bin/env  python3

import os
import glob
import json

directory = os.getcwd()
for file_name in glob.glob(f"{directory}/BOOKSMARKS/*"):
    with open(file=file_name, mode="r") as file:
        file_contents = file.read()
        json_data = json.loads(file_contents)

    with open(file=f"{directory}/bookmarks.txt", mode="a") as bookfile:
        for bookmark in json_data["roots"]["bookmark_bar"]["children"]:
            print()
            print(bookmark["name"])
            print(bookmark["url"])
            print()

            bookfile.write(f"{bookmark['name']}\n")
            bookfile.write(f"{bookmark['url']}\n")
            bookfile.write(f"\n")


print(type(json_data))
