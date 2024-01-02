#!/usr/bin/python3
"""The information list for a given employee ID"""
import requests
import sys


def get_todo_list_progress(employee_id):
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    response = requests.get(api_url)
    user_data = response.json()

    td_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todo_response = requests.get(td_url)
    todo_data = todo_response.json()
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    print(f"Employee {user_data['name']} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")

    for task in todo_data:
        if task['completed']:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list_progress(employee_id)
