#!/usr/bin/python3
"""Python script that returns information about
an employee's TODO list progress
"""
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    users_url = '{}/users/{}'.format(url, sys.argv[1])
    response = requests.get(users_url)
    json_data = response.json()
    print("Employee {} is done with tasks".format(
        json_data.get('name')), end="")

    todo_url = '{}todos?userID={}'.format(url, sys.argv[1])
    todo_res = requests.get(todo_url)
    tasks = todo_res.json()
    completed_tasks = []

    for task in tasks:
        if task.get('completed') is True:
            completed_tasks.append(task)

    print("({}/{}):".format(len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
