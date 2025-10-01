passwords = {}

while True:
    print("\n1. Add Password\n2. View Accounts\n3. Get Password\n4. Delete Account\n5. Exit")
    choice = int(input("Choose option: "))

    if choice == 1:
        acc = input("Enter account name: ")
        pwd = input("Enter password: ")
        passwords[acc] = pwd
    elif choice == 2:
        print("Accounts:", list(passwords.keys()))
    elif choice == 3:
        acc = input("Enter account name: ")
        print("Password:", passwords.get(acc, "Not found"))
    elif choice == 4:
        acc = input("Enter account name to delete: ")
        if acc in passwords:
            del passwords[acc]
            print("Deleted.")
        else:
            print("Not found.")
    elif choice == 5:
        break
