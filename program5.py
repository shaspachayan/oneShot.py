""" Develop a program that manages a contact list.
Allow users to add new contacts, view existing ones, and search for contacts by name."""


def add_contact(contact_list, name, phone_number):
    contact = {'name': name, 'phone_number': phone_number}
    contact_list.append(contact)
    print(f"Contact '{name}' added successfully!")


def view_contacts(contact_list):
    if not contact_list:
        print("Contact list is empty.")
    else:
        print("Contacts:")
        for idx, contact in enumerate(contact_list, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone_number']}")


def search_contact(contact_list, name):
    matching_contacts = [contact for contact in contact_list if name.lower() in contact['name'].lower()]
    if matching_contacts:
        print("Matching contacts:")
        for idx, contact in enumerate(matching_contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone_number']}")
    else:
        print("No matching contacts found.")


def main():
    contact_list = []

    while True:
        print("\nMenu:")
        print("1: Add new contact")
        print("2: View contacts")
        print("3: Search contacts by name")
        print("4: Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            add_contact(contact_list, name, phone_number)
        elif choice == "2":
            view_contacts(contact_list)
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(contact_list, name)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
