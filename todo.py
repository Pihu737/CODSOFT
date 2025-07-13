todo_list = []

def add_task():
    task = input("Enter a task:  ")
    todo_list.append({"Task": task, "Status": "Pending"})
    print("New task added successfully!\n")

def view_task():
    print("Your todo list: ")
    if len(todo_list) == 0:
        print("No pending tasks!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")  

def remove_task():
    if len(todo_list) == 0:
        print("List is empty.")   
    else:
        try:
            search_index = int(input("Enter the task number that you want to remove: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task removed: {removed_task['Task']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

def mark_done():
    if len(todo_list) == 0:
        print("List is empty.")   
    else:
        try:
            search_index = int(input("Enter the task number that you want to mark as complete: ")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['Status'] = 'Done'
                print(f"Task '{todo_list[search_index]['Task']}' has been marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

def menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Mark task as done")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the application...")
            break
        else:
            print("Invalid choice! Try again.")

menu()
