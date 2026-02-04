# creating contact book

def add_contact(name:str,number:int):
    # check name is exists in ph_book or not
    #get file contacts
    try :
        with open('contacts.txt','r') as f:
            contact_lines = f.readlines()
    except FileNotFoundError : 
        return 'error in add contacts'
    for contact in contact_lines:
        contact_name,*contact_number = contact.split()
        if contact_name == name:
            return  "contact name already exists"
    #add contact details to file
        try :
            with open('contacts.txt','a') as f:
                f.write(f"\n{name}{number}")
                return "contact added successfully"
        except : 
            return 'error in add contacts'

no = 9098909890
name="ramyaaaa"
print(add_contact(name=name,number = no))




# # update mobile no. in ph_book
# def update_number(name:str,number:int):
#      if name not in ph_book:
#         print("contact not exists")
#      else :
#         ph_book.update = ({name:number}) # updating mobile number
#         print("mobile number is updated")
# # delete contact 
# def delete_contact(name:str):
#     if name in ph_book:
#         ph_book.pop(name)
#         print("successfully deleted")
#     else:
#         print("contact not found")
# # To get a contact no.
# def get_number(name:str):
#     if name in ph_book:
#         number = ph_book.get(name, 'name is not found')
#         print("The contact number update is:", number)
# # print all contacts
# def all_contacts( ):
#     # if contact book is empty
#     if not ph_book:
#         print("no contacts found")
#     for name,number in ph_book.items( ):
#         print(f'{name} : {number}')

# # main
# def main():
#     print("Welcome to the Contact Book")

#     while True:
#         print("\n1. Add Contact")
#         print("2. Delete Contact")
#         print("3. Get Contact Number")
#         print("4. View All Contacts")
#         print("5. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             name = input("Enter name: ")
#             number = input("Enter number: ")
#             add_contact(name, number)

#         elif choice == "2":
#             name = input("Enter name to delete: ")
#             delete_contact(name)

#         elif choice == "3":
#             name = input("Enter name to search: ")
#             get_number(name)

#         elif choice == "4":
#             all_contacts()

#         elif choice == "5":
#             print("Thank you for using contact book")
#             break

#         else:
#             print("Invalid choice")

# main()