# To-Do List Application

# Empty list for storing tasks
todo_list = []

# Function to display all tasks
def show_tasks():
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("Your tasks:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to add a task
def add_task(task):
    todo_list.append(task)
    print(f"'{task}' added to the to-do list!")

# Main loop to take user input
while True:
    print("\nTo-Do List Options:")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter a new task: ")
        add_task(task)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
