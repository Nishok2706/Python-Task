###Write a program create class India,USA,UK
###Describe the country name in the constructor
###Describe the capital in capital function
###Describe the language in language function
class India:
    def __init__(self):
        self.country = "India"
    def capital(self):
        print("The capital of", self.country, "is New Delhi")
    def language(self):
        print("The national language of", self.country, "is Hindi")
class USA:
    def __init__(self):
        self.country = "USA"
    def capital(self):
        print("The capital of", self.country, "is Washington D.C")
    def language(self):
        print("The national language of", self.country, "is English")
class UK:
    def __init__(self):
        self.country = "UK"
    def capital(self):
        print("The capital of", self.country, "is London")
    def language(self):
        print("The national language of", self.country, "is English")
obj_india = India()
obj_usa = USA()
obj_uk = UK()
for country in (obj_india, obj_usa, obj_uk):
    country.capital()
    country.language()
    print()  
