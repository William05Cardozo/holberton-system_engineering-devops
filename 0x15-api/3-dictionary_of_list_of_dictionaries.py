#!/usr/bin/python3
"""This script export the info. on a other archived"""
import json
import requests

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users/')
    user_dict = {}
    user_dict2 = {}
    for user in users.json():
        uid = user.get("id")
        user_dict[uid] = []
        user_dict2[uid] = user.get("username")
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for task in todos.json():
            task_dict = {}
            uid = task.get("userId")
            task_dict["task"] = task.get('title')
            task_dict["completed"] = task.get('completed')
            task_dict["username"] = user_dict2.get(uid)
            user_dict.get(uid).append(task_dict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
