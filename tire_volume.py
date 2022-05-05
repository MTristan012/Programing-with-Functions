"""
MTristan 
26/04/2022
"""

import math
from datetime import datetime

actualTime = datetime.now()

width = int(input("Enter the width of the tire in mm(ex 205): "))
ratio = int(input("Enter the aspect ratio of the tire(ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches(ex 15): "))

volume = ((math.pi)*(width**2)*ratio *
          (width * ratio + 2540*diameter))/10000000000

print()
#I take prices from this page https://www.discounttire.com/
if width == 205 and ratio == 60 and diameter == 15:
    print("For these dimensions the price is $60/ea")
elif width > 205 and ratio > 60 and diameter > 15:
    print("For these dimensions the price is $252/ea")
elif width < 205 and ratio < 60 and diameter <15:
    print("For these dimensions the price is $97/ea")
else:
    print("For these dimensions the price is $129/ea")

print()
print(f"The approximate volume is {volume:.2f} liters")

print()
buyIt = input("Do You want to BUY tires with this dimensions?: ").lower()

if buyIt == "yes":
    phoneNumber = int(input("What is Your Phone Number?: "))
    print("We appreciate your preference, an operator will contact you")
    with open("volumes.txt", "at") as volumesFiles:
        print(f"{actualTime:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}, {phoneNumber}",file=volumesFiles)
else:
    with open("volumes.txt", "at") as volumesFiles:
        print(f"{actualTime:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}", file=volumesFiles)