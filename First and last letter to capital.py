###convert the first and last letter to capital
name=input("Enter the name: ")
print(name[0].upper()+name[1:-1]+name[-1].upper())
