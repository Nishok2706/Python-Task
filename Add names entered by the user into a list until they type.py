###Add names entered by the user into a list until they type 'stop'.
name=[]
while True:
    list = input("Enter the names (type'stop' to end): ")
    if list.lower()=='stop':
     break
    name.append(list)
print("Entered names are:",name)
    
