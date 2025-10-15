###Remove a specific item from a list entered by the user.

cities = ["Madurai","Chennai","Coimbatore","Nagercoil","Salem"]
user = input("Enter the city you want to remove:Madurai/Chennai/Coimbatore/Nagercoil/Salem: ")
if user in cities:
    cities.remove(user)
    print("The updated cities are:",cities)
else:
    print("You have entered the incorrect city name")


