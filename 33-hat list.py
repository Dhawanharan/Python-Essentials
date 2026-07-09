#write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
#write a line of code that removes the last element from the list (Step 2)
#write a line of code that prints the length of the existing list (Step 3).

hat_list = [1,2,3,4,5]
replace_number = int(input("Enter the number to replace : "))

mid =(len(hat_list)//2)+1
hat_list[mid] = replace_number

del hat_list[-1]
print(len(hat_list))
print(hat_list)
