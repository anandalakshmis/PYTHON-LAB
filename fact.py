num=int(input("enter the value:"))
def fact(num):
    fact = 1

    if num==0 or num==1:
        return 1
    for i in range(1,num+1):
        fact=fact*i
    return fact
fact (num)
print("fact of",num,"is:", fact(num))
