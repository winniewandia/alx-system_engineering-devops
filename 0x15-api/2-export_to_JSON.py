#!/usr/bin/python3
"""Python script that returns information about
an employee's TODO list progress
"""
import json
import requests
import sys

if __name__ == '__main__':
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    response = requests.get(todos_url).json()
    users_response = requests.get(users_url).json()
    name_id = sys.argv[1]
    name = None
    for j in users_response:
        if j['id'] == int(sys.argv[1]):
            name = j['username']
    task_list = []
    for i in response:
        if i['userId'] == int(sys.argv[1]):
            employee_dict = {
                "task": i['title'], "completed": i['completed'],
                "username": name}
            task_list.append(employee_dict)

    dict_task = {str(name_id): task_list}
    with open('{}.json'.format(name_id), mode='w') as f:
        json.dump(dict_task, f)
