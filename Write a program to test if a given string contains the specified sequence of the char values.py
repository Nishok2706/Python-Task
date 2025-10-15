#Write a program to test if a given string contains the specified sequence of the char values
A = input("Enter the sentence: ")
B = input("Enter the checking word: ")
if B in A:
    print("The word is found")
else:
    print("The word is not found")
