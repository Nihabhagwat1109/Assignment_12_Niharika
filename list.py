while True:
    print("Group management")
    print("1. Enroll yourself")
    print("2. See your group")
    print("3. See your group members' position")
    print("4. Allot various tasks to your group members")
    print("5. See their tasks")
    print("6. Exit")

    try:
     choice = int(input("Enter your choice: "))
     if choice == 1:
        import User_Enrollment
        User_Enrollment.User_Enrollment()
     if choice == 2:
        import see_group
        see_group.see_group()
     if choice == 3:
        import see_Roles
        see_Roles.see_Roles()
     if choice == 4:
        import task_manage
        task_manage.tasks()
     if choice == 5:
        import see_task
        see_task.see_task()
     if choice == 6:
        exit()
    except Exception as e:
        print("Invalid choice! Please try again.")    