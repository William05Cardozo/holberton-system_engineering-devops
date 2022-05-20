#!/usr/bin/python3
"""This script using a REST API"""
import requests
from sys import argv
i = 0
j = 0
if __name__ == "__main__":
    url = requests.get('https://jsonplaceholder.typicode.com/users/' +
                       argv[1])
    url_json = url.json()
    task = ""
    todo = requests.get('https://jsonplaceholder.typicode.com/todo')
    for t in todo.json():
        if t.get('userId') == int(argvv[1]):
            if t['completed']:
                task += "\t " + t['title'] + '\n'
                i += 1
            j += 1
    print("Employee {} is done with task({}/{}):".format(
           url_json['name'], i, j))
    print(task, end='')
