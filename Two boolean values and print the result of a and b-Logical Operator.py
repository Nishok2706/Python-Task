###Ask the user for two boolean values (True/False) and print the result of a and b.
a = input("Enter the first boolean value (True/False): ")
b = input("Enter the second boolean value (True/False): ")
a = True if a == "True" else False
b = True if b == "True" else False
result = a and b
print("The result of a and b is:", result)
