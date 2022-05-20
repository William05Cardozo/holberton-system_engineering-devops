#!/usr/bin/python3
"""This script using a REST API"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        argv[1])
    user_dic = user.json()
    user = user_dic["username"]
    task2 = []
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for t in todos.json():
        if t.get("userId") == int(argv[1]):
            task = {}
            task["user_id"] = t["userId"]
            task["username"] = user
            task["completed"] = t["completed"]
            task["title"] = t["title"]
            task2.append(task)

    try:
        id = "{}.csv".format(argv[1])
        with open(id, "w") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for element in task2:
                line = [element["user_id"], element["username"],
                        element["completed"], element["title"]]
                writer.writerow(line)
    except IOError:
        print("I/O error")
