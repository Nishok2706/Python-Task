###Program to read the temperature in centigrade and display a suitable message according to the temperature state below
###temp<0 then freezing weather
###temp 0-10 then very cold weather
###temp 10-20 then cold weather
###temp 20-30 then normal in temp
###temp 30-40 then its hot
###temp >=40 then its very hot

Temperature=int(input("Enter the temperature: "))
if Temperature <0:
    print("Freezing weather")
elif Temperature <=10:
    print("Very cold weather")
elif Temperature <=20:
    print("Cold weather")
elif Temperature <=30:
    print("Normal")
elif Temperature <40:
    print("Hot")
else:
    print("Very hot")
