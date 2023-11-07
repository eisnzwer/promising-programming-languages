phone_book = {}

num_contacts = int(input("Enter the number of contacts: "))

for _ in range(num_contacts):
    name = input("Enter the contact's name: ")
    number = input("Enter the phone number: ")
    phone_book[name] = number

name_list = list(phone_book.keys())

print("List of names from the phone book:", name_list)
