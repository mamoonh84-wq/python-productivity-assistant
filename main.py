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
    print(f"You chose: {choice}")

    print("-----------------------------------------")

    if choice == "1":
        task = input("Enter your task: ")
        print("Task added!")
        tasks.append(task)
    elif choice == "2":
        print("Your tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    elif choice == "4":
        break


    break