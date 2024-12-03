user = "aymn"
userpass = "aymn123"

userid = input("Username : ")
password = input("Password : ")

while True:

    if userid == user and password == userpass:
        print("Login Sucessful")
        break
    elif userid == user and password != userpass:
        print("password wrong")
        
    elif userid != user and password != userpass:
        print("user and password are wrong")
    else:
        print("error")
    

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")
    

def deposit():
    amount = float(input("amount to be deposited: "))
    if amount < 0:
        print("invalid amount")
        return 0 
    else:
        return amount

def withdraw(balance):
    amount = float(input("amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient Amount")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0 
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:

        print("Banking system")
        print("1.Show-Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.exit")

        choice = input("select form the following (1-4): ")

        if choice == '1':
                show_balance(balance)
        elif choice == '2':
                balance += deposit()
        elif choice == '3':
                balance -= withdraw(balance)
        elif choice == '4':
                is_running = False
                print("Thankyou have a nice day!")
        else:
            print("Invalid")

if __name__ == '__main__':
    main()
