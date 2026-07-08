#lists
#def list
numbers = [10,5,7,2,1]
print("Original list contents: ",numbers)

numbers[0] = 111
print("Updated list contents: ",numbers) #index strt form 0

#copying a value
numbers[1] = numbers[4]
print("After copying: ",numbers)

#access list content
print(numbers[3])

#list length
print("Length : ", len(numbers))

#deleting an element
del numbers[0]
print(len(numbers))

#accessing the last element can be done by -1
print("Last element : ",numbers[-1])
