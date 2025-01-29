#2. Write a Python program to remove a newline in Python String = "\nBest \nDeeptech \nPython \nTraining\n" 

str = "\nBest \nDeeptech \nPython \nTraining\n"
print(str)

clean = str.replace("\n","")
print("Clean String:",clean)