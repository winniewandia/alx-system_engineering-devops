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

    todos_response = requests.get(todos_url).json()
    users_response = requests.get(users_url).json()

    task_list = []
    dict_task = {}
    for user in users_response:
        user_id = user['id']
        user_name = user['username']
        for i in todos_response:
            my_dict = {"username": user_name,
                       "task": i['title'], "completed": i['completed']}
            task_list.append(my_dict)
        dict_task[str(user_id)] = task_list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(dict_task, f)
