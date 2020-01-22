#  The program should calculate how much water, coffee beans, and milk are necessary to make the specified amount of coffee.
#  One cup of coffee made on this coffee machine contains 200 ml of water, 50 ml of milk, and 15 g of coffee beans.
water = 200
milk = 50
beans = 15

print("Write how many cups of coffee you will need:")
am_cups = int(input())

print("For", am_cups, "cups of coffee you will need:")
water *= am_cups
milk *= am_cups
beans *= am_cups

print(water, "ml of water")
print(milk, "ml of milk")
print(beans, "g of coffee beans")

#  print("Starting to make a coffee")
#  print("Grinding coffee beans")
#  print("Boiling water")
#  print("Mixing boiled water with crushed coffee beans")
#  print("Pouring coffee into the cup")
#  print("Pouring some milk into the cup")
#  print("Coffee is ready!")