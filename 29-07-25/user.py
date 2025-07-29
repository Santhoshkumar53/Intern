import json
import os

FILE_NAME = 'users.json'

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    

def save_data(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)

def search_user(data):
    user_id = input("Enter User ID to search: ")
    user = data.get(user_id)
    if user:
        print("User Found:", user)
    else:
        print("User not found.")

def add_user(data):
    user_id = input("Enter new User ID: ")
    if user_id in data:
        print("User ID already exists.")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    email = input("Enter Email: ")
    data[user_id] = {"name": name, "age": age, "email": email}
    print("User added successfully.")

def delete_user(data):
    user_id = input("Enter User ID to delete: ")
    if user_id in data:
        del data[user_id]
        print("User deleted successfully.")
    else:
        print("User not found.")
def main():
    data = load_data()
    while True:
        print("\n--- User Manager ---")
        print("1. Search User")
        print("2. Add User")
        print("3. Delete User")
        print("4. Save & Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            search_user(data)
        elif choice == '2':
            add_user(data)
        elif choice == '3':
            delete_user(data)
        elif choice == '4':
            save_data(data)
            print("Data saved. Exiting.")
            break
        else:
            print("Invalid choice. Try again.")


main()
