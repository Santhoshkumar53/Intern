import csv
import os

FILE_NAME = 'tasks.csv'

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Task'])  

def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append({'ID': int(row['ID']), 'Task': row['Task']})
    except Exception as e:
        print("Error loading tasks:", e)
    return tasks

def save_tasks(tasks):
    try:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Task'])
            for task in tasks:
                writer.writerow([task['ID'], task['Task']])
    except Exception as e:
        print("Error saving tasks:", e)

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
    else:
        print("\n--- Your To-Do List ---")
        for task in tasks:
            print(f"{task['ID']}. {task['Task']}")
        print()

def add_task(tasks):
    task_text = input("Enter task: ").strip()
    if task_text:
        new_id = tasks[-1]['ID'] + 1 if tasks else 1
        tasks.append({'ID': new_id, 'Task': task_text})
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: "))
        updated_tasks = [task for task in tasks if task['ID'] != task_id]
        if len(updated_tasks) != len(tasks):
            save_tasks(updated_tasks)
            print("Task deleted successfully.")
        else:
            print("Task ID not found.")
        return updated_tasks
    except ValueError:
        print("Invalid input. Please enter a number.")
    return tasks

def update_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to update: "))
        for task in tasks:
            if task['ID'] == task_id:
                new_task = input("Enter new task: ").strip()
                if new_task:
                    task['Task'] = new_task
                    save_tasks(tasks)
                    print("Task updated successfully.")
                else:
                    print("Task cannot be empty.")
                return
        print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    initialize_file()
    tasks = load_tasks()

    while True:
        print("\n/*/*/*/* To-Do Menu */*/*/*/")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Exit")

        choice = input("Pick Your Choice (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            tasks = load_tasks()
        elif choice == '3':
            tasks = delete_task(tasks)
        elif choice == '4':
            update_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
