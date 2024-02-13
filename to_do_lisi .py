tasks = []

def add_task(description):
    tasks.append({"description": description, "completed": False})

def view_tasks():
    if not tasks:
        print("No tasks")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Incomplete"
            print(f"{i}. {task['description']} - {status}")

def mark_task_complete(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number")

def delete_task(task_number):
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task deleted.")
    else:
        print("Invalid task number")

def update_task_description(task_number, new_description):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["description"] = new_description
        print("Task description updated.")
    else:
        print("Invalid task number")

def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Update Task Description")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
            print("Task added.")
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to mark as complete: "))
            mark_task_complete(task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == "5":
            task_number = int(input("Enter task number to update: "))
            new_description = input("Enter new task description: ")
            update_task_description(task_number, new_description)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
