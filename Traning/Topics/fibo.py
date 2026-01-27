def fibo(n):
    ft = 0
    st = 1
    i = 1

    print(ft,st,end=" ")

    while i<=n-2:
        tt=ft+st
        print(tt)
        ft = st
        st = tt
        i = i+1

n = int(input("Enter how many terms:"))
fibo(n)