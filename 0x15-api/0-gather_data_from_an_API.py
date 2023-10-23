#!/usr/bin/python3
"""Python script that returns information about
an employee's TODO list progress
"""
import requests
import sys

if __name__ == '__main__':
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    todos_count = 0
    todos_complete = 0

    response = requests.get(todos_url).json()
    users_response = requests.get(users_url).json()
    name = None
    todos_title = []
    for i in users_response:
        if i['id'] == int(sys.argv[1]):
            name = i['name']

    for i in response:
        if i['userId'] == int(sys.argv[1]):
            todos_count += 1
        if i['completed'] and i['userId'] == int(sys.argv[1]):
            todos_complete += 1
            todos_title.append(i['title'])

    print("Employee {} is done with tasks({}/{}):".format(name,
          todos_complete, todos_count))

    for i in todos_title:
        print("\t {}".format(i))
