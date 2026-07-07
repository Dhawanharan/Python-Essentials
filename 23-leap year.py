#if the year number isn't divisible by four, it's a common year;
#otherwise, if the year number isn't divisible by 100, it's a leap year;
#otherwise, if the year number isn't divisible by 400, it's a common year;
#otherwise, it's a leap year.

year = int(input("Enter the year : "))
if year%4!=0 : print("Common year")
elif year%100!= 0: print("Common year")
elif year%400!=0: print("Common year")
else: print("leap year")
           
