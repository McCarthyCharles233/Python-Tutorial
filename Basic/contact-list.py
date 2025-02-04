
contacts = {}

while True:
    action = input("Input an action(add, view, search, delete, exit): ").strip().lower()

    if action == "add":
        key = input("Input name: ").strip()
        if key == "":
            print("Name cannot be empty.")
            continue
        value = input("Enter phone number: ").strip()
        if value == "":
            print("Phone number cannot be empty.")
            continue

        contacts[key] = value
        print(f"Contact '{key}' added successfully!")

    elif action == "view":
        if not contacts:
            print("No available contacts")
        else:
            print("\nSaved Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif action == "search":
        if not contacts:
            print("No available contacts")
        else:
            search = input("Input the name of the contact: ").strip()
            if search in contacts:
                print(f'{search}: {contacts[search]}')
            else:
                print("Name not found")

    elif action == "delete":
        if not contacts:
            print("No available contacts")
        else:
            search = input("Input the name of the contact: ")
            if search in contacts:
                contacts.pop(search)
                print(f"Contact '{search}' deleted successfully.")
            else:
                print("Name not found")

    elif action == "exit":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid action. Please enter 'add', 'view', 'search', 'delete', or 'exit'.")