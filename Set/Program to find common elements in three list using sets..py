###Program to find common elements in three list using sets.

Fruits_1 = {"Apple","Banana","Grapes","Guava","Cherry"}
Fruits_2 = {"Watermelon","Grapes","Guava","Strawberry","Blueberry"}
Fruits_3 = {"Rasberry","Pineapple","Guava"}
Fruits = Fruits_1.intersection(Fruits_2).intersection(Fruits_3)
print(Fruits)
