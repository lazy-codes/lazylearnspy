# ATM Simulation

balance = 10000
pin = "1234"
attempts = 3

# PIN Verification
while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")

    if entered_pin == pin:
        print("\nLogin Successful!")
        break
    else:
        attempts -= 1
        print("Incorrect PIN!")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Your account has been locked.")
    exit()

# ATM Menu
while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print(f"Current Balance: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))
        if amount > 0:
            balance += amount
            print("Deposit Successful!")
            print(f"New Balance: ₹{balance}")
        else:
            print("Invalid amount!")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))
        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient Balance!")
        else:
            balance -= amount
            print("Withdrawal Successful!")
            print(f"Remaining Balance: ₹{balance}")

    elif choice == "4":
        current_pin = input("Enter current PIN: ")
        if current_pin == pin:
            new_pin = input("Enter new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin
                print("PIN changed successfully!")
            else:
                print("PIN must be exactly 4 digits!")
        else:
            print("Incorrect current PIN!")

    elif choice == "5":
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid choice! Please select 1-5.")