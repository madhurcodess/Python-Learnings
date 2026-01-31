# 153 = 1*1*1 + 5*5*5 + 3*3*3
# 153 =   1   +   125 +   27 


def armstrong(n):
    sum = 0
    r=0
    while n>0:
        r = n%10
        sum=sum+(r*r*r)
        n=n//10
    return sum

n = int(input("Enter your number:"))
sum = armstrong(n)

if n==sum:
    print(f"{n} is armstrong")
else:
    print(f"{n} is not armstrong")