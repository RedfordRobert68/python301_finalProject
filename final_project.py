import os
import re

class Bank:

    def __init__(self):
        self.balance = 0
        # opening_balance = 100.00
        # with open(f"{self.user_name}.txt", "r") as transactions:
        #     transactions = transactions.readlines()

        # for transaction in transactions:
        #     print(transaction.rstrip())
        
        # print(type(transactions))
        # balance = 0

    # def newBalance(self):
    #     self.new_balance = self.balance + self.opening_balance

    def userName(self):
        self.user_name = input("Please enter your username: ")

    # User choices
    def userInput(self):
        user_input = input("\nWhat would you like to do?\n\t View Transactions (T) \n\t View Balance (B) \n\t Make a Withdrawal (W) \n\t Make a Deposit (D) \n\t Logout (L) \nEnter choice: ")
        return user_input

    
    # View Transactions
    def Transaction(self):
        with open(f"{self.user_name}.txt", "r") as transactions:
            transactions = transactions.readlines()
        # print(str(transactions))

        for transaction in transactions:
            print(transaction.rstrip())
            # print(transaction)
            # try:
            #     trans = re.sub(r'[^[0-9.-]', '', transaction)
            #     trans = int(float(trans))
            #     print(trans)
            #     # print(type(trans))
            #     # print(type(transaction))
            #     # print(transaction)
            # except:
            #     print("")
        print(f"_____________________________________\nBalance:\t\t{self.balance}")
        self.balance = int(self.balance)
       

    # Make Withdrawal
    def Withdrawal(self):
        # print("This is a withdrawal.")
        withdrawal = input("How much will you be withdrawing today? ")
        try:
            withdrawal = float(withdrawal)
            with open(f"{self.user_name}.txt", "a") as file:
      
                if withdrawal > 0 and withdrawal <= self.balance:
                    self.balance = self.balance - withdrawal
                    file.write(f"\nwithdrawal: \t\t-{withdrawal}")
                    print(f"\n${withdrawal} was withdrawn.")
                elif withdrawal > self.balance:
                    print("Your withdrawal request exceeds your balance. Please try again.")
                    pass
                elif withdrawal < 0:
                    print("You must enter an amount greater than zero")

        except ValueError:
            print("\nPlease use numbers and decimal only.")

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
            elif(deposit == "+" or deposit == "-"):
                print("Invalid entry!")
            
            else:
                print("You must enter an amount greater than zero")

        except ValueError:
            print("\nPlease use numbers and decimal only.")

    # View Balance
    def Balance(self):
        print(f"\nBalance:\t\t{self.balance}")
        # print(type(self.balance))


    # Logoout
    def Logout(self):
        quit()
        

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
        else:
            print("\nYour selection is invalid. Try again.")

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






    

