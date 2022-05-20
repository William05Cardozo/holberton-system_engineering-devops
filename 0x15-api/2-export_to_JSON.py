#!/usr/bin/python3
"""This script export the info. in a archived JSON"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        argv[1])
    user_json = user.json()
    task = ""
    dicto = {}
    listt = []
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for t in todos.json():
        if t.get("userId") == int(argv[1]):
            dicto2 = {}
            dicto2["task"] = t["title"]
            dicto2["completed"] = t["completed"]
            dicto2["username"] = user_json["username"]
            listt.append(dicto2)
            dicto[t["userId"]] = listt
    filename = argv[1] + ".json"
    with open(filename, "w") as outfile:
        json.dump(dicto, outfile)
