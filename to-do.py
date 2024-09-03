def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(tasks):
    if tasks:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks to show.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
