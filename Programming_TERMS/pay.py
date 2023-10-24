from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_type):
        self.security_type = security_type

    def pay(self, order):
        print("processing debit payment type")
        print(f"verifying security code: {self.security_type}")
        order.status = 'paid'

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_type):
        self.security_type = security_type

    def pay(self, order):
        print("processing credit payment type")
        print(f"verifying security code: {self.security_type}")
        order.status = 'paid'

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_add):
        self.email_add = email_add

    def pay(self, order):
        print("processing Paypal payment type")
        print(f"verifying security code: {self.email_add}")
        order.status = 'paid'