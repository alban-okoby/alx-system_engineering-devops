#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests


def get_all_employees_todo():
    users_url = 'https://jsonplaceholder.typicode.com/users'
    users_response = requests.get(users_url)
    users_data = users_response.json()

    all_tasks = {}

    for user in users_data:
        user_id = str(user['id'])
        td_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
        todo_response = requests.get(td_url)
        todo_data = todo_response.json()

        user_tasks = [
            {"username": user['username'], "task": task['title'],
                "completed": task['completed']}
            for task in todo_data
        ]

        all_tasks[user_id] = user_tasks

    json_file_path = 'todo_all_employees.json'
    with open(json_file_path, 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)

    print(f"\nData exported to {json_file_path}")


if __name__ == "__main__":
    get_all_employees_todo()
