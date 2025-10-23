###program to remove the intersection of a 2nd set from the 1set

Fruits_1 = {"Apple","Banana","Grapes","Guava","Cherry"}
Fruits_2 = {"Watermelon","Grapes","Guava","Strawberry","Blueberry"}
Fruits_1.difference_update(Fruits_2)
print(Fruits_1)
