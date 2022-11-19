def pair(a):
    count=0
    for sock in set(a):
        tcount=a.count(sock)
        count+=tcount//2
    return count
arr=[10,20,20,10,10,30,50,10,20,20,50]
print(pair(arr))
