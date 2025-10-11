###Write a program that iterates the integers from 1 to 50.
###For multiples of three prints "Fizz" instead of the number.
###For multiples of five prints "Buzz" instead of the number.
###For numbers which are multiples of both three and five print"FizzBuzz"
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
