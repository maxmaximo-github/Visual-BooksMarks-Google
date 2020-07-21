#!/usr/bin/env  python3

import os
import get
import json


with open(file="Bookmarks", mode="r") as file:
    file_contents = file.read()
    json_data = json.loads(file_contents)


print(type(json_data))

with open(file="bookmarks.txt", mode="w") as bookfile:
    for bookmark in json_data["roots"]["bookmark_bar"]["children"]:
        print()
        print(bookmark["name"])
        print(bookmark["url"])
        print()

        bookfile.write(f"{bookmark['name']}\n")
        bookfile.write(f"{bookmark['url']}\n")
        bookfile.write(f"\n")
