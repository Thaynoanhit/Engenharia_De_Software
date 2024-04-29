# Implementações concretas
class CreditCardPaymentProcessor:
    def process_payment(self, amount):
        print(f"Processando pagamento de R$ {amount} com cartão de crédito")

class PayPalPaymentProcessor:
    def process_payment(self, amount):
        print(f"Processando pagamento de R$ {amount} com PayPal")

# Classe que depende de implementações concretas
class PaymentGateway:
    def __init__(self, payment_processor):
        if payment_processor == "CreditCard":
            self.payment_processor = CreditCardPaymentProcessor()
        elif payment_processor == "PayPal":
            self.payment_processor = PayPalPaymentProcessor()
        else:
            raise ValueError("Processador de pagamento inválido")

    def make_payment(self, amount):
        self.payment_processor.process_payment(amount)

# Exemplo de uso
payment_gateway = PaymentGateway("CreditCard")
payment_gateway.make_payment(100.0)

payment_gateway = PaymentGateway("PayPal")
payment_gateway.make_payment(50.0)