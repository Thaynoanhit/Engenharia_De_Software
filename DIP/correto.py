# Abstração
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Método process_payment() deve ser implementado nas subclasses.")

# Implementações concretas
class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processando pagamento de R$ {amount} com cartão de crédito")

class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processando pagamento de R$ {amount} com PayPal")

# Classe que depende da abstração
class PaymentGateway:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def make_payment(self, amount):
        self.payment_processor.process_payment(amount)

# Exemplo de uso
payment_gateway = PaymentGateway(CreditCardPaymentProcessor())
payment_gateway.make_payment(100.0)

payment_gateway = PaymentGateway(PayPalPaymentProcessor())
payment_gateway.make_payment(50.0)