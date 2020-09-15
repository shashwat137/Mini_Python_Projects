'''
Makes an unique account number that stores the account holder name, amount deposited and manages credits and debits of
each account holder.
'''
# debit ->  (withdrawal)
# credit -> (deposited)

import time
import secret # File contains bank manager credentials

class Account():
    '''
    Will maintain the functionality and treat each account at a separate object.
    '''
    def __init__(self,name, account_number):
        '''
        name will be a string.
        '''
        self.name = name
        self.balance = 0 # Will hold amount of money present.
        self.account_number = account_number # Will be an auto incremented integer. Also unique.

    def __str__(self):
        return f"Account Number {self.account_number}, Account Holder {self.name}, Account Balance {self.balance}"

    def debit(self, amount):
        self.balance -= amount

    def credit(self, amount):
        self.balance += amount

    def view(self):
        return self.balance

    def remove(self):
        return f"The Account of {self.name} having Account Number {self.account_number} with balance {self.balance} was deleted."

def make_account(account_number):
    '''
    Creates an instance for given account number. Account number must be unique.
    '''
    name = input("Enter your Name\n")
    return Account(name, account_number)

def transact_account(account_instance, command):
    '''
    account account_instance is an object of Account
    Command lets us know if we have to debit or credit.
    '''
    if command == 1: # Debit
        while True:
            amount = input("Enter the amount to be Debited.\n")
            try:
                amount = float(amount)
                if amount > account_instance.view():
                    print("You cannot Debit more than your balance.\nPlease enter value again.")
                    continue
                else:
                    account_instance.debit(amount)
                    break
            except:
                print("Enter a valid amount to be debited")
                continue
        print(f"{amount} has been credited to your account. You now have a balance of {account_instance.view()}")
    elif command == 2: # Credit
        while True:
            amount = input("Enter the amount to be Credited.\n")
            try :
                amount = float(amount)
                break
            except:
                print("Enter a valid amount to be credited")
                continue
        account_instance.credit(amount)
        print(f"{amount} has been credited to your account. You now have a balance of {account_instance.view()}")
    else:
        pass
    return

def verification():
    password = input('Enter the bank manager password.\n')
    if password == secret.hold_password():
        return True
    else:
        return False

def manager(database):
    print("Entries in the database are as follows\n")
    for k in database:
        print(database[k])
    return

def main():
    account_number = 12345      # Starting account number, to be incremented when new account is made. Value is dummy.
    account_data = dict() # This will hold all the bank data and keyed using account number.
    print("Select what you wish to do")
    while True:
        # key_name = None # Initially program is not to be quit. This is used to go back to main menu
        while True:
            command1 = input("\nMain Menu\n\nEnter 1 for making an account\nEnter 2 for viewing your account\nEnter 3 for transacting your account\nEnter 4 to delete your account.\nEnter 5 to exit\n")
            try:
                command1 = int(command1)
                if command1 > 0 and command1 <= 5:
                    break
                else:
                    print("You must enter only a Valid Input")
                    continue
            except:
                print("You must enter only a Valid Input")
                continue
        if command1 == 1:
            account_data[account_number] = make_account(account_number)
            print(f"Account created.\n{account_data[account_number]}")
            account_number += 1 # Increments the account number, ensuring that it is unique.
            time.sleep(1)
        elif command1 == 2:
            while True:
                key_name = input("Enter your valid account number.\nEnter q to go back to main menu.\n")
                if key_name.lower() == 'q':
                    time.sleep(0.5)
                    break
                else:
                    try:
                        print(account_data[int(key_name)])
                        time.sleep(1)
                        break
                    except:
                        print("Please Enter a valid account number")
                        time.sleep(0.5)
                        continue
        elif command1 == 3:
            while True:
                key_name = input("Enter your valid account number.\nEnter q to go back to main menu.\n")
                if key_name.lower() == 'q':
                    break
                else:
                    try:
                        account_instance = account_data[int(key_name)]
                        break
                    except:
                        print("Please Enter a valid account number")
                        time.sleep(0.5)
                        continue
            if key_name == 'q':
                time.sleep(0.5)
                continue
            while True:
                command2 = input("Enter 1 to debit your account\nEnter 2 to Credit your account\nEnter q to go back to main menu.\n")
                if command2 == 'q':
                    break
                try:
                    command2 = int(command2)
                    if command2 >= 1 and command2 <= 2:
                        break
                    else:
                        print("Please enter a valid input")
                        time.sleep(0.5)
                        continue
                except:
                    print("Please enter a valid input")
                    continue
            if command2 == 'q':
                time.sleep(0.5)
                continue
            transact_account(account_instance, command2)
            time.sleep(1)
        elif command1 == 4:
            while True:
                key_name = input("Enter your valid account number to delete.\nEnter q to go back to main menu.\n")
                if key_name.lower() == 'q':
                    time.sleep(0.5)
                    break
                else:
                    try:
                        deleted_account = account_data.pop(int(key_name))
                        print(deleted_account.remove())
                        time.sleep(1)
                        break
                    except:
                        print("Please Enter a valid account number")
                        time.sleep(0.5)
                        continue
        elif command1 == 5:
            print("Thank you for using our banking services\nHave a nice day.")
            time.sleep(1)
            break
        else:
            pass
    return account_data

if __name__ == "__main__":
    database = main()
    while True:
        final = input('Enter y to log into bank manager account\nEnter q to quit\n')
        if final.lower() == 'y':
            if verification():
                print("Password Verified.")
                time.sleep(2)
                manager(database)
                break
            else:
                print("Sorry incorrect password. You may try again\n")
                continue
        elif final.lower() == 'q':
            break
        else:
            print("Invalid Input. Please try again.")
            continue
