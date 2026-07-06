#let's find the largest of three numbers
num1 = int(input("Enter num 1 : "))
num2 = int(input("Enter num 2 : "))
num3 = int(input("Enter num 3 : "))

largest = num1

if num2>largest: largest = num2
if num3>largest: largest = num3

print("The largest number is : ", largest)
        
