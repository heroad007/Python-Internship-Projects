from myfunc import *

while True:
    print()
    print("----Employee Management System-----")
    print()
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Display Employees")
    print("5. Exit")
    print()
    choice = input("Select anyone: ")
    if choice == '1':
        add_employee()
        print()
    elif choice == '2':
        update_employee()
        print()
    elif choice == '3':
        delete_employee()
        print()
    elif choice == '4':
        display_employees()
        print()
    elif choice == '5':
        print('Exit from program')
        break
    else:
        print("Invalid Option.")

