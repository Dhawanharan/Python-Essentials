beatles = []
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for i in range (2):
    mm = input("Enter member : ")
    beatles.append(mm)
print("Step 3:", beatles)

del beatles[3]
del beatles[4]
print("Step 4:", beatles)

beatles.insert("Ringo Starr")
print("Step 5:", beatles)
