c0 = int(input("Enter any non-negative and non-zero number"))
while c0 !=1:
    if c0%2==0:
        c0 = c0//2
        print(c0)
    else:
        c0 = 3*c0+1
        print(int(c0))
         
