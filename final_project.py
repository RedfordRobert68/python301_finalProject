import os


class Bank:

    def __init__(self, opening_balance = 100.00):
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
            print(transaction.rstrip())

    # Make Withdrawal
    def Withdrawal(self):
        # print("This is a withdrawal.")
        withdrawal = input("How much will you be withdrawing today? ")
        try:
            withdrawal = float(withdrawal)
            with open(f"{self.user_name}.txt", "a") as file:
                file.write(f"\nwithdrawal: \t\t-{withdrawal}")
                print(f"\n${withdrawal} was withdrawn.")
        except ValueError:
            print("\nPlease use numbers and decimal only.")

        if withdrawal:
            if withdrawal > 0:
                self.balance = self.balance - withdrawal
            else:
                print("You must enter an amount greater than zero")

    # Make Deposit
    def Deposit(self):
        # print("This is a deposit.")
        deposit = input("How much will you be depositing today? ")
        try:
            deposit = float(deposit)
            with open(f"{self.user_name}.txt", "a") as file:
                file.write(f"\nDeposit: \t\t+{deposit}")
                print(f"\n${deposit} was deposited.")

            if deposit > 0:
                self.balance = self.balance + deposit
            
            else:
                print("You must enter an amount greater than zero")

        except ValueError:
            print("\nPlease use numbers and decimal only.")

    # View Balance
    def Balance(self):
        print(f"Balance:\t\t{self.balance}")


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
            quit()

def login():
    while True:
        # If username is empty
        account.userName()

        if(account.user_name.lower() == ""):
            pass

        # Welcome message
        elif(os.path.exists(f"{account.user_name}.txt")):
            print(f"\nWelcome {account.user_name},")
            options()

        # New users start with $100.00
        else:
            with open(f'{account.user_name}.txt', 'w') as file:
                file.write(f"\nOpening balance: \t {account.balance}")
                # with open(f"{self.user_name}.txt", "r") as file:
                #     balance = file.read()
                # print(balance)
            print(f"\nWelcome {account.user_name},")
            options()
login()






    

