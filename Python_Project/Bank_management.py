print("---User details---")
input1 = input("Enter user name : ")
input2 = input("Enter user address : ")
print("User name : ",input1)
print("User Address : ",input2)

def show_balance(balance):
    print(f"Your balance is {balance:.2f} TK")
    
def deposit():
    amount = float(input("Enter an amount to be deposited : "))
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("Enter an amount to be withdraw : "))
    if amount > balance:
        print("Insuficiant Balance")
        return 0
    elif amount < 0:
        print("Amount must be greater then zero(0)")
        return 0
    else:
        return amount
    
def main():
    balance = 0
    is_running = True
    while is_running:

        print("---Banking Program---")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice(1-4) : ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("This is not a valid choice")
    print("Thank you for whih us")

if __name__ == '__main__':
    main()
