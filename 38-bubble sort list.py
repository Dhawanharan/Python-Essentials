#sorting list-bubbble sort
my_list = []
num = int(input("How many elements: "))

for i in range(num):
    val = int(input("Enter value : "))
    my_list.append(val)
    
print(my_list)
swapped = True

while swapped:
    swapped = False
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            swapped = True
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            
print("Sorted list : ",my_list)
