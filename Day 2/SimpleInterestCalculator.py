#4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.

Principal = int(input("Enter Principal Amount: "))
Time = int(input("Enter Term in years: "))
RoI = float(input("Enter Rate of Interest(one year): "))
TRoI = RoI*Time

TSI = (Principal*TRoI)/100
print("Total Interest: ",TSI)

EB = Principal+TSI
print("End Balance: ",EB)
