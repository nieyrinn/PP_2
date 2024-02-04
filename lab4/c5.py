class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            print("Insufficient funds. Withdrawal amount exceeds the available balance.")

# Пример использования
account_owner = input()
initial_balance = float(input())

account = BankAccount(owner=account_owner, balance=initial_balance)

# Депозиты
account.deposit(100)
account.deposit(50)

# Вывод средств
account.withdraw(30)
account.withdraw(200)  # Попытка снять больше, чем доступно
