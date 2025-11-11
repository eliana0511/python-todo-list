# To-Do List App (Simple CLI Version)
# Author: Ally 
# Description: A simple Python program to manage daily tasks.

tasks = []

def show_menu():
    print("\n📝 To-Do List Menu")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Mark task as complete")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. {task['name']} {status}")

def add_task():
    name = input("\nEnter a new task: ")
    tasks.append({'name': name, 'done': False})
    print(f"Task '{name}' added!")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"Removed task: {removed['name']}")
    except (ValueError, IndexError):
        print("Invalid task number!")

def mark_complete():
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to mark as complete: "))
        tasks[task_num - 1]['done'] = True
        print(f"Task '{tasks[task_num - 1]['name']}' marked complete!")
    except (ValueError, IndexError):
        print("Invalid task number!")

while True:
    show_menu()
    choice = input("\nChoose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        mark_complete()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
