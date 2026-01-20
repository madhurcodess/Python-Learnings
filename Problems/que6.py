# Input - Student Name, Marks & Percentage of student and display appropriate grade.
#    validations- Percent should not 100% , Zero, Negative  


name = str(input("Enter your Name:"))
marks = int(input("Enter your Marks:"))
percent = float(input("Enter your Percentage:"))
   
    
if percent == 100 :
    print("Percentage should not be 100%.")
elif percent <= 0:
    print("Percentage should not be 0 or negative.")
else:
    print(f"Hi {name}.")
    print(f"You got {marks} Marks.")
    print(f"And you got {percent} Percentage")



if percent < 40:
    print("Fail")
elif percent > 90:
    print("You got A+ Grade")
elif percent > 80:
    print("You got A Grade")
elif percent > 60 :
    print("You got B Grade")
elif percent > 40 :
    print("You got C Grade")
else :
    print("Should not be Negative or Zero")























