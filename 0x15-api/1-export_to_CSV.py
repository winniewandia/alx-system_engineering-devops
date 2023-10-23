#!/usr/bin/python3
"""Python script that returns information about
an employee's TODO list progress
"""
import csv
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
            task_list.append(
                [i['userId'], name, i['completed'], i['title']])

    with open('{}.csv'.format(name_id), mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for task in task_list:
            writer.writerow(task)
