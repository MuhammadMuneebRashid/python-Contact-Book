# Store the contacts in Dictionary
contacts={}
# Function to add a new contact
def add_contact():
    name=input("Enter the name:")
    number=int(input("Enter the number:"))
    contacts[name]=number
    print("contact added successfully!")
# Function to view all contacts    
def view_contact():
    if(len(contacts))==0:
        print("No contact available")
    else:
    # Display all the contacts 
        print("\n Contacts") 
        for name,number in contacts.items():
            print(name,"-",number)
# Function to search a contact            
def search_contact():
    name=input("Enter the name to search:")
    if (name in contacts):
        print("number :" , contacts[name])
    else:
        print("no record found") 
# Function to delete a contact         
def delete_contact():
    name=input("Enter the name to delete :")  
    if (name in contacts):
        del contacts[name]
        print("contact is deleted")
    else:
        print("no record found") 
# Keep the program running until the user  exists         
while True:
    print("=== Contact Book ===")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    # Take input from the user
    choice=int(input("Enter the choice:"))
    # Call the add contact function
    if(choice==1):
        add_contact()
    # Call the view all contacts function   
    elif(choice==2):
        view_contact()
    # Call the search contact function
    elif(choice==3):
       search_contact()
    # Call the delete contact function  
    elif(choice==4):
        delete_contact()
    # Exit the program    
    elif(choice==5):
        print("Good Bye!")
        break
    # Handles Invalid input
    else:
        print("Invalid choice")                    
              
