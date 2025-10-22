###Find the key found in Diction using arbitary Keyword Arguement
def found(**details):
    for key,value in details.items():
        print("Key",key,"value is",value)
found(Name = "Nishok",Age = 27, Location = "Chennai", Contact = 9952605893)
