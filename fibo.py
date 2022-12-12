num=int(input("Enter the value:"))
print("the fibonacci series is:")
def fibo(num):
    n1=0
    n2=1
    count=0
    print(n2)
    while(count<num-2):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
        count=count+1
fibo(num)
