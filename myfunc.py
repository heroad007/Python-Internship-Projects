list_of_employees=[]

def add_employee():
    check=True
    print('Enter Employee Details')
    id=int(input('ID:'))
    name=input('Name:')
    age=input('Age:')
    position=input('Position:')
    salary=int(input('Salary:'))

    if not list_of_employees:
        check=True
    else:
        for employee in list_of_employees:
            if id==employee['id']:
                check=False
                break

    if check==True:
        employee={
            'id':id,
            'name':name,
            'age':age,
            'position':position,
            'salary':salary
        }
        list_of_employees.append(employee)
        print('Employee added successfully')
    else:
        print('ID already exists.')

def update_employee():
    id=int(input('Enter ID:'))
    for employee in list_of_employees:
        if id == employee['id']:
            print('Which information you want to update:')
            print('1. Name')
            print('2. Position')
            print('3. Salary')
            ch=input('Select any one to update:')
            if ch=='1':
                print(f'Name:{employee['name']}')
                employee['name']=input('Enter new name:')
            elif ch=='2':
                print(f'Position:{employee['position']}')
                employee['position']=input('Enter new position:')
            elif ch=='3':
                print(f'Salary:{employee['salary']}')
                employee['salary']=input('Enter new salary:')
            else:
                print('Invalid choice.')

            print('employee detail updated successfully')
            print()
            return
    print('Employee not found')

def delete_employee():
    id = int(input('Enter ID:'))
    for employee in list_of_employees:
        if id == employee['id']:
            list_of_employees.remove(employee)
            print('Employee deleted successfully')
            return
    print('Employee not found')

def display_employees():
    if len(list_of_employees)==0:
        print('No employee to display')
        return
    print('ID \t\t Name \t\t Age \t\t Position \t\t Salary')
    for employee in list_of_employees:
        print(f'{employee['id']} \t\t {employee['name']} \t\t {employee['age']} \t\t {employee['position']} \t\t {employee['salary']}')
