def fib(n):
    a=0 
    b =1
    print(a)
    print(b)
    for i in range(2,n):
        t=b
        b+=a
        a=t
        print(b)
n = int(input())
fib(n)


