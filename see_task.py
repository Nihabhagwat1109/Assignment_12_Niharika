def see_task():
    f=open("tasks.txt","r")
    tasks=f.read()
    print(f"Your tasks are: {tasks}")