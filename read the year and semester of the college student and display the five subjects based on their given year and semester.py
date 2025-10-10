###program to read the year and semester of the college student and display the five subjects based on their given year and semester.
year=int(input("Enter the year 1/2/3/4: "))
semester = int(input("Enter the semester 1/2: "))
if year ==1 and semester==1:
    print("Engineering Physics1,Engineering Chemistry1,Computer Programming,Mathematics-1,Engineering Graphics")
if year ==1 and semester ==2:
    print("Engineering Physics2,Engineering Chemistry2,Mathematics-2,Basic Electrical and Electronics Engineering,Engineering Mechanics")
if year ==2 and semester ==1:
    print("Mathematics-3,Signals and Systems,Objected Oriented Programming,Electronic Devices and Circuits,Digital Engineering")
if year ==2 and semester ==2:
    print("Mathematics-4,Control Systems,Electromagnetic Fields,Linear Integrated Circuits,Linear Integrated Circuits Lab")
if year ==3 and semester ==1:
    print("Environmental Science,Digital Communications,Transmission Line and Waveguides,Digital Signal Processing,Digital Signal Processing Lab")
if year ==3 and semester ==2:
    print("VLSI Designs,Microprocessor and Microcontroller,Microprocessor and Microcontroller Lab,Antenna and Wave Propagation,Computer Networks")
if year ==4 and semester ==1:
    print("RF & Microwave Engineering,Optical Communication & Networks,Embedded & Real Time Systems,Profession Ethics,Microwave Lab Embedded Design Lab")
if year ==4 and semester ==2:
    print("Wireless Communication,Wireless Networks,Final Year Project,Wireless Communication Lab,Wireless Networks Lab")
else:
    print("Enter valid data")
