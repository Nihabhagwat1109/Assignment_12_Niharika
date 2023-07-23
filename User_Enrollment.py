def User_Enrollment():
    name=input("Enter your name: ")
    password=int(input("Enter your password: "))
    Role=input("Enter your role in group: ")

    if name == 'Niharika' and password == 1234:
        f = open("data.txt","+at")
        f.write("Welcome User!\n")
        f.write(f"name: {name}\n password: {password}\n Role: {Role}")
    else:
        print("Invalid details")
