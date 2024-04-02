def discount(price, discount):
  if (discount >= 20):
    price -= price * (discount / 100)
  else:
    pass
  return price

price = float(input("Enter the price: "))
disc = float(input("Enter the discount: "))
discount(price, disc)
