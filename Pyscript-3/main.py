#my_dict = {'Name':[]}

contactbook = {'kenil':[1212121244,4554545455],'abhay':[4589631278]}

#to add contact (name and number both)
def add_contact():
    name = input("Enter Name : ")
    no = int((input("how many mobile number are you want to add : ")))
    id = 0
    list=[]
    while no:
        print("mobile no ",id+1," : ")
        list.append(int(input()))
        no = no - 1
        id = id + 1
    contactbook[name]=list 
    

#to display all contact 
def all_contacts_list():
    if contactbook:
        for x in contactbook:
            print (x)
            no = int(len(contactbook[x]))
            id = 0
            while no:
                print ('\t\t','moblile no ',id+1,' ',contactbook[x][id])
                id = id +1
                no = no -1
    else:
        print("No contact detail in contact book")

#to find contact using name
def find_contact():
    name = input("enter the name of person : ")
    if not system_find_number(name):
        print("we have no any contact save with this name : ",name)
        return
    for x in contactbook:
        if(x == name):
            print (x)
            no = int(len(contactbook[x]))
            id = 0
            while no:
                print ('\t\t','moblile no ',id+1,' ',contactbook[x][id])
                id = id +1
                no = no -1

# this function is for system like if i enter any number in for any opration then this is check name was saved or not saved 
def system_find_number(name):
    c = False
    for x in contactbook:
        if(x == name):
            c = True
    return c

# this fuction if for delete contact (name and all number)
def delete_contact():
    name = input("enter the name of person : ")
    if not system_find_number(name):
        print("we have no any contact save with this name : ",name)
        return
    contactbook.pop(name)

# this function is for edit name which was saved in our contactkeeper
def Edit_name():
    o_name = input("enter the incorrect name of person : ")
    if not system_find_number(o_name):
        print("we have no any contact save with this name : ",o_name)
        return
    n_name = input("enter the correct name of person : ")
    for x in contactbook:
        if(x == o_name):
            list = contactbook[o_name]
    contactbook[n_name] = list
    contactbook.pop(o_name)

# this function is for change mobile number
def change_mobile_number(name):
    for x in contactbook:
        if(x == name):
            print (x)
            no = int(len(contactbook[x]))
            id = 0
            while no:
                print ('\t\t','moblile no ',id+1,' ',contactbook[x][id])
                id = id +1
                no = no -1        
    id = int(input("give the id of number which you are tring to change : "))
    number = int(input("Enter new number : "))
    contactbook[name].remove(contactbook[name][id-1])
    contactbook[name].append(number)

# this function is for delete any one mobile number
def delete_mobile_number(name):
    for x in contactbook:
        if(x == name):
            print (x)
            no = int(len(contactbook[x]))
            id = 0
            while no:
                print ('\t\t','moblile no ',id+1,' ',contactbook[x][id])
                id = id +1
                no = no -1
    id = int(input("give the id of number which you are tring to delete : "))
    contactbook[name].remove(contactbook[name][id-1])

# this function is for add one mobile number in saved contact
def add_mobile_number(name):
    number = int(input("Enter the number which you want to add : "))
    contactbook[name].append(number)

# this function is for edit mobile number
def edit_mobile_number():
    name = input("enter the name of person whose are you tring to edit : ")
    if not system_find_number(name):
        print("we have no any contact save with this name : ",name)
        return

    while 1:
        print("1. change contact \n2. delete contacts \n3. add mobile number")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            change_mobile_number(name)
            break
        elif choice == 2:
            delete_mobile_number(name)
            break
        elif choice == 3:
            add_mobile_number(name)
            break
        else:
            print("Invalid Choice")

#menu
while 1:
    print("\n")
    print("1. Add a new contact \n2. View all contacts \n3. Find a contact\n4. Delete a contact\n5. Modify a name\n6. Modify a number\n7. Exit")

    choice = int(input("Enter your choice : "))
    print("\n")

    if choice == 1:
        add_contact()
    elif choice == 2:
        contactbook =  dict(sorted(contactbook.items()))
        all_contacts_list()
    elif choice == 3:
        find_contact()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        Edit_name()
    elif choice == 6:
        edit_mobile_number()
    elif choice == 7:
        break
    else:
        print("Invalid Choice")
    
