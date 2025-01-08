# 4. A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.
# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.
# On orders of more than Rs. 100 for key-based toys, a discount of 5% is given,
# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.
# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.
# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

ProductCode = int(input("Enter a Product Code: "))

if ProductCode == 1:
	BatteryPrice = int(input("Enter Amount: "))
	if BatteryPrice>=1000:
		Discount = BatteryPrice*10/100
		NetPrice = BatteryPrice - Discount
		print("Your Net Amount is:",NetPrice)
	else:
		print("Your Net Amount is:",BatteryPrice)


if ProductCode == 2:
	KeyPrice = int(input("Enter Amount: "))
	if KeyPrice>=100:
		Discount = KeyPrice*5/100
		NetPrice = KeyPrice - Discount
		print("Your Net Amount is:",NetPrice)
	else:
		print("Your Net Amount is:",KeyPrice)


if ProductCode == 3:
	ElectricalPrice = int(input("Enter Amount: "))
	if ElectricalPrice>=500:
		Discount = KeyPrice*10/100
		NetPrice = ElectricalPrice - Discount
		print("Your Net Amount is:",NetPrice)
	else:
		print("Your Net Amount is:",ElectricalPrice)