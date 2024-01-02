#!/usr/bin/python3
"""Export to JSON"""
import requests
import sys
import json


def get_todo_list_progress(employee_id):
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(api_url)
    user_data = response.json()

    td_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todo_response = requests.get(td_url)
    todo_data = todo_response.json()

    json_data = {
        str(user_data['id']): [
            {"task": task['title'], "completed": task['completed'],
                "username": user_data['username']}
            for task in todo_data
        ]
    }

    print(f"Employee {user_data['name']} is done with tasks"
          f"({user_data['id']}/{len(todo_data)}):")

    json_file_path = f"{user_data['id']}.json"
    with open(json_file_path, 'w') as jsonfile:
        json.dump(json_data, jsonfile)

    print(f"\nData exported to {json_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list_progress(employee_id)
