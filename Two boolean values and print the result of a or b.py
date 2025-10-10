###Ask the user for two boolean values and print the result of a or b.
a = input("Enter the first boolean value (True/False): ")
b = input("Enter the second boolean value (True/False): ")
a = True if a == "True" else False
b = True if b == "True" else False
result = a or b
print("The result of a and b is:", result)
