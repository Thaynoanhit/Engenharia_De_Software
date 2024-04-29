# Classe que só tem uma responsabilidade: gerenciar o saldo de um usuário
class UserBalance:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Saldo insuficiente")

# Classe que só tem uma responsabilidade: autenticar um usuário
class UserAuthenticator:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            return True
        else:
            return False

# Classe que só tem uma responsabilidade: gerenciar as informações de um usuário
class UserInfo:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

# Exemplo de uso
user_balance = UserBalance()
user_authenticator = UserAuthenticator("hit", "password123")
user_info = UserInfo("Hit Aguiar", "hit@example.com")

# Depositando dinheiro na conta do usuário
user_balance.deposit(100.0)

# Autenticando o usuário
if user_authenticator.authenticate("hit", "password123"):
    print("Usuário autenticado com sucesso!")
else:
    print("Erro ao autenticar usuário")

# Exibindo informações do usuário
print(f"Nome: {user_info.get_name()}, Email: {user_info.get_email()}")