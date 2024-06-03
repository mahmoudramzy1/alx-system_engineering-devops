#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import csv
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    todosurl = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    usersurl = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    filename = user_id + '.csv'

    usersresponse = requests.get(usersurl)
    name = usersresponse.json().get('username')

    todosresponse = requests.get(todosurl)
    todos = todosresponse.json()

    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos:
            writer.writerow([user_id, name, str(task.get('completed')),
                            task.get('title')])
