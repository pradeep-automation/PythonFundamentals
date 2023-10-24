# from pay import PaymentProcessor, DebitPaymentProcessor, PaypalPaymentProcessor
#
#
# class Order:
#     # class variables
#     items = []
#     quantities = []
#     prices = []
#     status = "open"
#
#     def add_item(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
#
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total
#
#     # def pay(self, payment_type, security_type):
#     #     if payment_type == 'debit':
#     #         print("processing debit payment type")
#     #         print(f"verifying security code: {security_type}")
#     #         self.status = 'paid'
#     #
#     #     elif payment_type == 'credit':
#     #         print("processing credit payment type")
#     #         print(f"verifying security code: {security_type}")
#     #         self.status = 'paid'
#     #     else:
#     #         raise Exception(f"unknown payment type: {payment_type}")
#
#
# order = Order()
# order.add_item("Keyboard", 2, 25)
# order.add_item("Mouse", 5, 12)
# order.add_item("Cable", 20, 5)
# print(order.total_price())
# # order.pay("debit", "0313456")
# payment_process = PaypalPaymentProcessor("pradeepramola152@gmail.com")
# payment_process.pay(order)
#
#
my_ls = [2, 7, 5, 3]
your_ls = [5, 3, 2, 7]
sort_my_list = sorted(my_ls)
your_ls.sort()
print(your_ls == sort_my_list)
