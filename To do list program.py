print(
    '''
    choose process to do:
    --[1] create task.
    --[2] show task.
    --[3] delete task.
    --[4] update task.
    '''
)

choose = int(input("Enter the number: \n"))

tasks = {
    'reading': 'inprocess',
    'writing': 'completed'
}

if choose == 1:
    new_task = input("Enter a task: ")
    tasks[new_task] = 'Inprocess'

    print("\n---Your tasks---")
    print("Task | Status")
    for x, y in tasks.items():
        print(x + " | " + y)

elif choose == 2:
    print("\n---Your tasks---")
    print("Task | Status")
    for x, y in tasks.items():
        print(x + " | " + y)

elif choose == 3:
    delete_task = input("Enter a task: ")
    if delete_task in tasks:
        del tasks[delete_task]
    else:
        print("Task is not found")

    print("\n---Your tasks---")
    print("Task | Status")
    for x, y in tasks.items():
        print(x + " | " + y)

elif choose == 4:
    print(
       '''
      choose status:
      --[1] Inprocess
      --[2] Completed
      --[3] Canceled
       '''
    )

    tk = input("Enter a task: ")
    if tk in tasks:
        ch = int(input("Enter a number: "))

        if ch == 1:
            tasks[tk] = 'Inprocess'
        elif ch == 2:
            tasks[tk] = 'Completed'
        elif ch == 3:
            tasks[tk] = 'Canceled'
        else:
            print("Invalid choice")
    else:
        print("Task is not found")

    print("\n---Your tasks---")
    print("Task | Status")
    for x, y in tasks.items():
        print(x + " | " + y)

else:
    print("Invalid choice")
