tasks = []

while True:
    print("My personal python productivity assistant")

    print("-----------------------------------------")

    print("1. Add a task")
    print("2. View tasks")
    print("3. Complete a task")
    print("4. Exit")

    print("-----------------------------------------")

    choice = input("Choose an option: ")

    print("-----------------------------------------")

    if choice == "1":
        task = input("Enter your task: ")
        print("Task added!")
        tasks.append({"title": task, "completed": False})
    elif choice == "2":
        print("Your tasks:")
        for i, task in enumerate(tasks, start =1):
            status = "✔️" if task["completed"] else " "
            print(f"{i}. [{status}] {task['title']}")
    elif choice == "3":
        if not tasks:
            print("You have no tasks to complete.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✔️" if task["completed"] else " "
                print(f"{i}. [{status}] {task['title']}")
            try:
                task_number = int(input("Enter the number of the task to complete: "))
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
                continue
            if 1 <= task_number <= len(tasks):
                task_index = task_number - 1
                tasks[task_index]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
    elif choice == "4":
        break