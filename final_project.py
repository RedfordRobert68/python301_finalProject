import os
import re

class Bank:

    user_name = ""

    def __init__(self, opening_balance = 0):
        self.balance = opening_balance

    def userName(self):
        self.user_name = input("Please enter your username: ")

    # User choices
    def userInput(self):
        user_input = input("\nWhat would you like to do?\n\t View Transactions (T) \n\t View Balance (B) \n\t Make a Withdrawal (W) \n\t Make a Deposit (D) \n\t Logout (L) \nEnter choice: ")
        return user_input

    
    # View Transactions
    def Transaction(self):
        # print("This is a transaction.")
        with open(f"{self.user_name}.txt", "r") as transactions:
            transactions = transactions.readlines()

        for transaction in transactions:

            # Remove Balance from being a transaction
            if transaction.find("Balance") != -1:
                pass
            else:
                print(transaction.rstrip())

        # Show balance after transactions
        print(f"___________________________________\nBalance:\t\t{round(self.balance, 2)}")

    # Make Withdrawal
    def Withdrawal(self):
       # print("This is a withdrawal.")
        withdrawal = input("How much will you be withdrawing today? ")
        try:
            withdrawal = float(withdrawal)
            with open(f"{self.user_name}.txt", "a") as file:
      
                if withdrawal > 0 and withdrawal <= self.balance:
                    self.balance = self.balance - withdrawal
                    file.write(f"\nwithdrawal: \t\t-{round(withdrawal, 2)}")
                    print(f"\n${withdrawal} was withdrawn.")
                elif withdrawal > 0:
                    print("\nYour withdrawal request exceeds your balance. Please try again.")
                    pass
                elif withdrawal < 0:
                    print("\nYou must enter an amount greater than zero")

        except ValueError:
            print("\nPlease use numbers and decimal only.")

    # Make Deposit
    def Deposit(self):
        # print("This is a deposit.")
        deposit = input("How much will you be depositing today? ")
        try:
            deposit = float(deposit)
            with open(f"{self.user_name}.txt", "a") as file:

                if deposit > 0:
                    self.balance = self.balance + deposit
                    file.write(f"\nDeposit: \t\t+{round(deposit, 2)}")
                    print(f"\n${deposit} was deposited.")
                
                else:
                    print("\nYou must enter an amount greater than zero!")
                    pass

        except ValueError:
            print("\nPlease use numbers and decimal only.")

    # View Balance
    def Balance(self):
        print(f"\nBalance:\t\t{round(self.balance, 2)}")

        # with open(f"{self.user_name}.txt", "a") as file:
        #     file.write(f"\nBalance: \t\t{round(self.balance, 2)}")

    # Capture the balance of returning customers
    def returningBalance(self):
        with open(f"{self.user_name}.txt", "r") as self.balance:
            self.balance = self.balance.readlines()[-1]
            self.balance = re.sub("[^0-9.]", " ", self.balance)
            self.balance = float(self.balance)
            # print(type(self.balance))
            # print(self.balance)
            # print(f"{round(balance, 2)}")

    # Logout - Write balance to text file for future use when user returns
    def Logout(self):
        with open(f"{self.user_name}.txt", "a") as file:
            file.write(f"\nBalance: \t\t{round(self.balance, 2)}")
        


account = Bank()

def options():
    while True:
        account_option = account.userInput()
        if account_option.lower() == "t":
            account.Transaction()
        elif account_option.lower() == "b":
            account.Balance()
        elif account_option.lower() == "d":
            account.Deposit()
        elif account_option.lower() == "w":
            account.Withdrawal()
        elif account_option.lower() == "l":
            account.Logout()
            break
        else:
            print("\nYour selection is invalid. Try again.")

def login():
    while True:
        # If username is empty
        account.userName()

        if(account.user_name.lower() == ""):
            pass

         # Welcome message for returning users
        elif(os.path.exists(f"{account.user_name}.txt")):
            print(f"\nWelcome {account.user_name}.")

            # This is where the returning balance code belongs
            account.returningBalance()


            # Show user options
            options()

        # New users start with $0
        else:
            with open(f'{account.user_name}.txt', 'w') as file:
                file.write(f"\nOpening balance: \t {account.balance}")
            print(f"\nWelcome {account.user_name},")

            # Show user options
            options()
login()






    

