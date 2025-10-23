###Count Vowels - Create a tuple of letters and count how many vowels are there using a loop.

vowels =tuple("Nishok")
count = 0
for i in vowels:
    if i.lower() in "aeiou":
     count+=1
print("The number of vowel is",count)



