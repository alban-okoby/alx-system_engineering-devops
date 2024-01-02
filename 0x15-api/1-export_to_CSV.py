#!/bin/usr/python3
"""Exports information list to CSV format"""
import requests
import sys
import csv


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

    csv_file_path = f"{user_data['id']}.csv"
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
            "TASK_TITLE"])

        for task in todo_data:
            csv_writer.writerow(
                    [user_data['id'], user_data['username'],
                        task['completed'], task['title']])
            if task['completed']:
                print(f"\t {task['title']}")
    print(f"\nData exported to {csv_file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list_progress(employee_id)
