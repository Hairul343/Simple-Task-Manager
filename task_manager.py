import os

def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file if line.strip()]
    return tasks

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        file.write("\n".join(tasks))

def list_tasks():
    tasks = load_tasks()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks yet!")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def mark_task_completed(task_index):
    tasks = load_tasks()
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] = f"{tasks[task_index - 1]} (Completed)"
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def delete_task(task_index):
    tasks = load_tasks()
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Deleted task: {deleted_task}")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nTask Manager Menu:")
        print("1. List tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            mark_task_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to delete: "))
            delete_task(task_index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
