# 5. A transport company charges the fare according to following table:
# 		Distance					Charges
# 		1-50						8 Rs/Km
# 		51-100						10 Rs/Km
# 		>100						12 Rs/Km

Distance = int(input("Enter Distance in Kilometers: "))

if Distance >= 1 and Distance <= 50:
	Charges = 8
	Fare = Charges*Distance
	print("Total Fare:",Fare)
elif Distance >= 51 and Distance <= 100:
	Charges = 10
	Fare = Charges*Distance
	print("Total Fare:",Fare)
elif Distance>100:
	Charges = 12
	Fare = Charges*Distance
	print("Total Fare:",Fare)
else:
	print("Invalid Journey Distance")