# 7. WAP to take year of experiance as a variable & display employee positons 
#     1. 0 - 1 = fresher 
#     2. 1 - 3 = senior
#     2. 3 - >3 = Teamlead

exp = float(input("Enter Your Experience:"))

if exp <= 1:
    print("You are a Fresher.")
elif exp <= 3:
    print("You are a Senior.")
else:
    print("You are a Teamlead.")