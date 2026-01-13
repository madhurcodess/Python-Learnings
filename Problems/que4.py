# Find Max of three Numbers 

num1 = int(input("Enter Number1:"))
num2 = int(input("Enter Number2:"))
num3 = int(input("Enter Number3:"))

if num1 > num2:
    print(f"{num1} is Greater.")
elif num2 > num3:
    print(f"{num2} is Greater.")
elif num1 > num3:
    print(f"{num1} is Greater.")
else:
    print(f"{num3} is Greater.")
    


