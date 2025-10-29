###Write a program create class Birds,Parrot,Sparrow
###Describe the birds name in constructor
###Descibe the bird name in constructor
###Describe the bird sounds make_sound function

class Bird:
  def __init__(self,name):
      self.name=name
  def make_sound(self):
      print(self.name,"makes a sound")
class Parrot(Bird):
    def make_sound(self):
        print(self.name, "says hello")
class Sparrow(Bird):
    def make_sound(self):
        print(self.name, "says sweetly hello")
parrot = Parrot("Parrot")
sparrow = Sparrow("Sparrow")
parrot.make_sound()
sparrow.make_sound()
        
