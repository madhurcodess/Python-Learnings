# stack = [1]

# stack.append(10)
# stack.append(20)
# print("Push",stack)

# stack.pop()
# print("Pop",stack)

# print("Peek",stack[-1])



# stack = []

# def push(item):
#     stack.append(item)
#     print(item, "pushed")

# push(10)

# def pop():
#     if  stack:
#         print(stack.pop(), "popped")
#     else:
#         print("Stack is empty")

# pop()


stack = []
def push():
    print("Enter the number:")
    item = int(input())
    stack.append(item)

def pop():
    if is_empty():
        print("Stack  is empty ")
    return stack.pop()

def peek():
    return stack[-1]

def display():
    print(stack)

def is_empty():
    return len(stack)==0

while True:

    print("1. push")
    print("2. pop")
    print("3. peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter Your Choice"))
    if ch == 1:
        push()

    elif ch == 2:
        pop()

    elif ch == 3:
        print(peek())

    elif ch == 4:
        display()

    elif ch == 5:
        break

    else:
        print("Invalid Input")

