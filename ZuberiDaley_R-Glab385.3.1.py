# R-Guided Lab 385.3.1 - Contact List Application Data Saved in File
# Zuberi Daley 

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
# Write the contact to the file
# do not forget to add a file path
    with open("contacts.txt", "a") as file:
        file.write(f"{name}: {phone}\n")
    print(f"{name} has been added to your contacts!")

def view_contacts():
    try:
        # Read the contacts from the file
        # do not forget to add a file path
        with open("contacts.txt", "r") as file:
          # here we are reading the file line by line
            contacts = file.readlines()
            # if the file is empty then contacts will be an empty list
            if not contacts:
                print("Your contact list is empty.")
            else:
                print("Your Contact List:")
                for contact in contacts:
                  # here we are removing the new line character
                  # and printing the contact
                    print(contact, end='')
    except FileNotFoundError:
        print("Your contact list is empty.")

def main():
    while True:
        print("\nContact List Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
# Call the main function
if __name__ == "__main__":
    main()