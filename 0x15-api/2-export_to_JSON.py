#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import json
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    todosurl = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    usersurl = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    filename = user_id + '.json'
    todouser = {}
    todotask = []

    usersresponse = requests.get(usersurl)
    name = usersresponse.json().get('username')

    todosresponse = requests.get(todosurl)
    todos = todosresponse.json()

    for task in todos:
        taskdict = {"task": task.get("title"),
                "completed": task.get("completed"),
                "username": name}
        todotask.append(taskdict)
    todouser[user_id] = todotask

    with open(filename, mode='w') as f:
        json.dump(todouser, f)
