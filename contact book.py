#CONTACT BOOK#

contact = []

#adding contacts
def add():
    name = input("Enter Contact Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    address = input("Enter the Address: ")
    if name and phone:
        contact.append({"Name":name,"Phone":phone,"Email":email,"Address":address})
        print("Addes Successfully!")
    else:
        print("Name and Phone number are required fields")

#viewing the contact
def view():
    if not contact:
        print("No Contacts")
    else:
        print("Contacts are")
        for contacts in contact:
            print(f"Name:{contacts['Name']}")
            print(f"Phone: {contacts['Phone']}")
            print(f"Email: {contacts['Email']}")
            print(f"Address: {contacts['Address']}")
            print("-"*30)

#searching of contact
def search(search_item):
    matches = [contacts for contacts in contact if search_item.lower() in contacts['Name'].lower() or search_item.lower() in contacts['Phone'].lower()]

    if not matches:
        print("No matching contacts")
    else:
        print("Matching Contacts")
        for match in matches:
            print(f"Name:{match['Name']}")
            print(f"Phone: {match['Phone']}")
            print(f"Email: {match['Email']}")
            print(f"Address: {match['Address']}")
            print("-"*30)

#delete of contact
def delete():
    search_item = input("Enter name of the contact to delete: ")
    matches = [contacts for contacts in contact if search_item.lower() in contacts['Name'].lower() or search_item.lower() in contacts['Phone'].lower()]
    if not matches:
        print("No matching contacts")
    else:
        for match in matches:
            contact.remove(match)
            print("Contact deleted Successfully!")

while True:
    print("\n")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == '1':
        add()
    elif choice == '2':
        view()
    elif choice == '3':
        search_item = input("Enter the name to search: ")
        search(search_item)
    elif choice == '4':
        delete()
    elif choice == '5':
        print("Bye")
        break
    else:
        print("Invalid Choice")
    




