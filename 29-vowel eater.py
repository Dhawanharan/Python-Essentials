#ask the user to enter a word;
#use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
#print the uneaten letters to the screen,

user_word = input("Enter the word : ")
user_word = user_word.upper()
word_without_vowels = ""

for letter in user_word:
    if letter =='A':
        continue
    if letter =='E':
        continue
    if letter =='I':
        continue
    if letter =='O':
        continue
    if letter =='U':
        continue
    word_without_vowels = word_without_vowels+letter
print(word_without_vowels)


                  
