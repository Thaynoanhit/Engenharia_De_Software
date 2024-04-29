class PaymentProcessor:
    def process_payment(self, amount):
        if amount < 100:
            print("Processando pagamento de R$ {} com cartão de crédito".format(amount))
        elif amount < 500:
            print("Processando pagamento de R$ {} com PayPal".format(amount))
        else:
            print("Processando pagamento de R$ {} com transferência bancária".format(amount))

class PaymentGateway:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def make_payment(self, amount):
        self.payment_processor.process_payment(amount)

# Exemplo de uso
payment_gateway = PaymentGateway(PaymentProcessor())
payment_gateway.make_payment(50)  # Output: Processando pagamento de R$ 50 com cartão de crédito
payment_gateway.make_payment(200)  # Output: Processando pagamento de R$ 200 com PayPal
payment_gateway.make_payment(1000)  # Output: Processando pagamento de R$ 1000 com transferência bancária