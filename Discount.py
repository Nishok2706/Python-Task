###A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
###Ask for user
###Judge and print total cost of user
Quantity=int(input("Enter the quantity: "))
if Quantity>1000:
    discount_amount = Quantity * 0.10
    Total_cost=Quantity - discount_amount
    print("Your order got 10% discount")
    print("Your total cost is",Total_cost)
else:
    print("Your total cost is",Quantity)
