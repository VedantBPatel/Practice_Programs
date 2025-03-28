import random
class Customer:
    def __init__(self,name,address,contact):
        self.name=name
        self.address=address
        self.contact=contact
        self.accounts=[]#empty list

    def create_acc(self,acc_type,initial_balance):
        account_number=Bank.generate_acc_num()
        account=BankAccount(acc_type,initial_balance,account_number)
        self.accounts.append(account)#this will go to self.accounts which is in customer class.

    def display_info(self):
        print(f"Name:{self.name}, Address:{self.address}, Contact:+91{self.contact}")
        for account in self.accounts:
            print(f"account:{account}")

class BankAccount:
    def __init__(self,acc_type,balance,acc_number):
        self.acc_type=acc_type
        self.balance=balance
        self.acc_number=acc_number

    def deposit(self,amount):
        self.balance+=amount
        print(f"Rupees{amount} was creadited to your account number:{self.acc_number}. Current balance is:{self.balance}")

    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Rupees{amount} was debited from your account number:{self.acc_number}. Current balance is:{self.balance}")
        else:
            print("Insufficient Funds!!!!!!")

    def __str__(self):
        return f"{self.acc_type}, Account:[No:{self.acc_number}, Balance:{self.balance}]"

class Bank:
    def __init__(self,name):
        self.name=name
        self.customers=[]#empty list
    
    def add_customer(self,customer):
        self.customers.append(customer)

    @staticmethod
    def generate_acc_num():
        return ''.join(random.choices('0123456789',k=8))
    
    def display_info(self):
        print(f"Bank:{self.name}")
        for customer in self.customers:
            customer.display_info()
    
    def find_acc(self,account_number):
        for customer in self.customers:
            for account in customer.accounts:
                if account.acc_number==account_number:
                    return account
        return None

# Interactive Menu


def main():
    bank = Bank("Tech Bank")
    while True:
        print("\nWelcome to Tech Bank")
        print("1. New Customer")
        print("2. Existing Customer")
        print("3. Display Bank Info")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            # Add a new customer
            name = input("Enter Customer Name: ")
            address = input("Enter Customer Address: ")
            contact = input("Enter Customer Contact: ")
            customer = Customer(name, address, contact)
            bank.add_customer(customer)
            print("\nCustomer added successfully!")
            acc_type = input("Enter Account Type (Savings/Current): ")
            initial_balance = float(input("Enter Initial Balance: "))
            customer.create_acc(acc_type, initial_balance)

        elif choice == '2':
            # Existing customer actions based on account number
            account_number = input("Enter Your Account Number: ")
            account, customer = bank.find_acc(account_number)
            if account:
                print(f"\nWelcome, {customer.name}!")
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Display Account Info")
                    print("4. Exit")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == '1':
                        # Deposit money
                        amount = float(input("Enter Amount to Deposit: "))
                        account.deposit(amount)

                    elif sub_choice == '2':
                        # Withdraw money
                        amount = float(input("Enter Amount to Withdraw: "))
                        account.withdraw(amount)

                    elif sub_choice == '3':
                        # Display account info
                        print("\nAccount Details:")
                        print(account)

                    elif sub_choice == '4':
                        # Exit to main menu
                        print("Exiting to main menu.")
                        break
                    else:
                        print("Invalid choice! Please try again.")
            else:
                print("Account not found!")

        elif choice == '3':
            # Display bank info
            bank.display_info()

        elif choice == '4':
            print("Thank you for using Tech Bank. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()


