import argparse
import json
import os

TASKS_FILE = "tasks.json"

if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as file:
        json.dump([], file)

def load_tasks():
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(args):
    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "task": args.task, "status": "pending"})
    save_tasks(tasks)
    print(f"Task added: {args.task}")

def list_tasks(args):
    tasks = load_tasks()
    for task in tasks:
        print(f"{task['id']}. {task['task']} - {task['status']}")

def update_task(args):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == args.id:
            task["task"] = args.task
            print(f"Task {args.id} updated to: {args.task}")
            break
    else:
        print("Task not found")
    save_tasks(tasks)

def delete_task(args):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != args.id]
    save_tasks(tasks)
    print(f"Task {args.id} deleted")

def main():
    parser = argparse.ArgumentParser(description="CLI To-do List Manager")
    subparsers = parser.add_subparsers()


    parser_add = subparsers.add_parser('add', help="Add a new task")
    parser_add.add_argument('task', type=str, help="The task to add")
    parser_add.set_defaults(func=add_task)

    
    parser_list = subparsers.add_parser('list', help="List all tasks")
    parser_list.set_defaults(func=list_tasks)


    parser_update = subparsers.add_parser('update', help="Update an existing task")
    parser_update.add_argument('id', type=int, help="The ID of the task to update")
    parser_update.add_argument('task', type=str, help="The new task description")
    parser_update.set_defaults(func=update_task)

    
    parser_delete = subparsers.add_parser('delete', help="Delete a task")
    parser_delete.add_argument('id', type=int, help="The ID of the task to delete")
    parser_delete.set_defaults(func=delete_task)

    
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
