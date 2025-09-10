START
  Make an empty list called tasks

  LOOP forever:
    Show menu:
      1. View tasks
      2. Add task
      3. Update task
      4. Delete task
      5. Exit

    Get user choice

    IF choice = 1 → show tasks
    IF choice = 2 → add a new task
    IF choice = 3 → update an existing task
    IF choice = 4 → delete a task
    IF choice = 5 → break loop

END
tasks = []   # empty list to store tasks

def show_menu():
    print("\n=== To-Do App ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)

def update_task():
    view_tasks()
    num = int(input("Enter task number to update: "))
    new = input("Enter new task: ")
    tasks[num-1] = new

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    tasks.pop(num-1)

# main loop
while True:
    show_menu()
    choice = input("Choose (1-5): ")

    if choice == "1": view_tasks()
    elif choice == "2": add_task()
    elif choice == "3": update_task()
    elif choice == "4": delete_task()
    elif choice == "5":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice!")