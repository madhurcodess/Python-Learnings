# Take input from user of three numbers and print average with validations 
# 1. should not -ve
# 2. number should not zero 
# 3. no string

num1 = int(input("Enter Number1:"))
num2 = int(input("Enter Number2:"))
num3 = int(input("Enter Number3:"))

average = (num1+num2+num3)/3

if (num1 or num2 or num3) <=0 :
    print("Number should not be Negative or Zero.")
else :
    print(average)
    
    