class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            new_account = BankAccount(account_number, initial_balance)
            self.accounts[account_number] = new_account
            return new_account
        return None

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

if __name__ == "__main__":
    bank = Bank()

    while True:
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            account = bank.create_account(account_number, initial_balance)
            if account:
                print("Account created successfully.")
            else:
                print("Account already exists.")

        elif choice == "2":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter amount to deposit: "))
                if account.deposit(amount):
                    print("Deposit successful.")
                else:
                    print("Invalid amount.")

        elif choice == "3":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                if account.withdraw(amount):
                    print("Withdrawal successful.")
                else:
                    print("Insufficient balance or invalid amount.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                print(f"Account balance: ${account.get_balance()}")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

