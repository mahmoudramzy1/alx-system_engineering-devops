#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

if __name__ == "__main__":

    complete = 0
    count = 0
    user_id = int(sys.argv[1])
    todosurl = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    usersurl = f'https://jsonplaceholder.typicode.com/users/{user_id}'

    usersresponse = requests.get(usersurl)
    users = usersresponse.json()

    todosresponse = requests.get(todosurl)
    todos = todosresponse.json()
    for todo in todos:
        count += 1
        if todo['completed'] is True:
            complete += 1
    print("Employee {} is done with tasks({}/{}):".format(
        users['name'], complete, count))

    if todos is not None:
        for todo in todos:
            if todo['completed'] is True:
                print(f"\t {todo['title']}")
