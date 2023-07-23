def tasks():
    tasks=input("Enter the tasks to be done:")
    file=open("tasks.txt","+a")
    file.write(tasks+"\n")
    print("task is entered")