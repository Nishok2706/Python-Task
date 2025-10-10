###A student will not be allowed to sit in exam if his/her attendance is less than 75%
classes_held = int(input("Enter number of classes held: "))
classes_attend = int(input("Enter number of classes attend: "))
Attendance = classes_held * 75/100
if classes_attend < Attendance:
    print("Student is not allowed to sit in exam")
else:
    print("Student is allowed to sit in exam")
