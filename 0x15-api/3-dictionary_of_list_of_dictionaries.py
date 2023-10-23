#!/usr/bin/python3
"""Python script that returns information about
an employee's TODO list progress
"""
import json
import requests
import sys

if __name__ == '__main__':
    from collections import defaultdict
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    users_response = requests.get(users_url).json()

    task_list = defaultdict(list)
    dict_task = {}
    for user in users_response:
        user_id = user['id']
        user_name = user['username']
        url = '{}?userId={}'.format(todos_url, user_id)
        todos_response = requests.get(url).json()
        for i in todos_response:
            my_dict = {"username": user_name,
                       "task": i['title'], "completed": i['completed']}
            task_list[i['userId']].append(my_dict)

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(task_list, f)
