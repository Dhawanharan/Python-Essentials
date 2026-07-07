#prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
#prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
#prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

name = input("Enter the string : ")
if name== "Spathiphyllum": print("Yes- Spathiphyllum is the best")
elif name == "spathiphyllum": print("No, I want a big Spathiphyllum")
else: print("Spathiphyllum! Not ",name,"!")
