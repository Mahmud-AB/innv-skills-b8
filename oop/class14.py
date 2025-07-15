class OrderSystem:
    def __init__(self,price,quantity,coupon_code=None):# multiple methods same name same class diffrenct parameters
        self.price = price
        self.quantity = quantity
        self.coupon_code = coupon_code

    def place_order(self):
        if self.coupon_code:
            print(f"Applying coupon code: {self.coupon_code}")
            # Here you would typically apply the coupon logic
            # For simplicity, let's assume it gives a 10% discount
            discount = self.price * 0.1
            self.price -= discount
            print(f"Discount applied: ${discount:.2f}")
        print(f"Order placed for {self.quantity} items at ${self.price} each.")

    def get_total_price(self):
        print(self.price * self.quantity)

class PowerOrderSystem(OrderSystem): 
    def __init__(self,price,quantity,coupon_code=None):
        self.price = price
        self.quantity = quantity
        self.coupon_code = coupon_code

    def place_order(self):# multiple methods same name diffrent class same parameters
        if self.coupon_code:
            print(f"Applying coupon code: {self.coupon_code}")
            # Here you would typically apply the coupon logic
            # For simplicity, let's assume it gives a 10% discount
            discount = self.price * 0.2
            self.price -= discount
            print(f"Discount applied: ${discount:.2f}")
        print(f"Order placed for {self.quantity} items at ${self.price} each.")
    


user1 = OrderSystem(100, 2, "DISCOUNT10")
user1.place_order()
user1.get_total_price()
user2 = OrderSystem(50, 1)
user2.place_order()

power_user1 = PowerOrderSystem(100, 3, "DISCOUNT10")
power_user1.place_order()
power_user1.get_total_price()
