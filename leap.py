year=int(input("enter the current year:"))
end=int(input("enter the end year:"))
print("the leap year are:")
for year in range(year,end+1):
    if((year&4==0)and year%100!=0 or year%400==0):
               print(year)
                     
