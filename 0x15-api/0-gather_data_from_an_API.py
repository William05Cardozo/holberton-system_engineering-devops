#!/usr/bin/python3
"""This script using a REST API"""
import requests
from sys import argv

i = 0
j = 0
if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        argv[1])
    user_json = user.json()
    task = ""
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            if t['completed']:
                task += "\t " + t['title'] + '\n'
                i += 1
            j += 1
    print("Employee {} is done with tasks({}/{}):".format(
           user_json['name'], i, j))
    print(task, end='')
