class User:
    def __init__(self, name, email, username, password, balance=0):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.balance = balance

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Saldo insuficiente")

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_balance(self):
        return self.balance