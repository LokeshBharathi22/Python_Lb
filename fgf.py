# Define functions for your to-do list app
def add_task(tasks, task):
    tasks[task] = False
    print("Task added:", task)

def view_tasks(tasks):
    if tasks:
        print("Tasks:")
        for index, (task, completed) in enumerate(tasks.items(), start=1):
            print(f"{index}. {'[X]' if completed else '[ ]'} {task}")
    else:
        print("No tasks found.")

def mark_completed(tasks, index):
    if 1 <= index <= len(tasks):
        task_to_mark = list(tasks.keys())[index - 1]
        tasks[task_to_mark] = True
        print(f"Task '{task_to_mark}' marked as completed.")
    else:
        print("Invalid task index.")

# Define the main function to run the to-do list app
def main():
    print("Welcome to Simple To-Do List App!")
    tasks = {}

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")

        if choice == '4':
            print("Exiting...")
            break

        elif choice == '1':
            task = input("Enter task: ")
            add_task(tasks, task)

        elif choice == '2':
            view_tasks(tasks)

        elif choice == '3':
            view_tasks(tasks)
            index = int(input("Enter the index of the task to mark as completed: "))
            mark_completed(tasks, index)

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Entry point of the application
if __name__ == "__main__":
    main()
