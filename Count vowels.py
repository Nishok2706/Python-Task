###How to count vowels in a string?

Input = input("Enter the string: ")
String=Input.lower()
count = 0
for i in String:
    if i in "aeiou":
     count+=1
print("The number of vowel is",count)
    
