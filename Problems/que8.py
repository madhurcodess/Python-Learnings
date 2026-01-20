# 8. Print stars '*' in Right angle Triangle 


rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()   