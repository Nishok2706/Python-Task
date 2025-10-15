###How to remove all digits from a string?

string = "My age is 27 and my 1998"
remove =""
for i in string:
    if not i.isdigit():
        remove+=i
print(remove)

