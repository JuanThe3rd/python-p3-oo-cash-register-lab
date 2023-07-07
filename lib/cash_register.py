#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.price = price
    self.quantity = quantity
    if quantity > 1:
      for i in range(quantity):
        self.items.append(title)
    else:
      self.items.append(title)
  
  def apply_discount(self):
    self.total *= 1 - (self.discount * 0.01)
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def items(self):
    return self.items
  
  def void_last_transaction(self):
    if self.quantity > 1:
      for i in range(self.quantity):
        self.total -= self.price
    else:
      self.total -= self.price

test = CashRegister()
test.discount = 20
test.add_item("macbook", 1000)
test.apply_discount()
