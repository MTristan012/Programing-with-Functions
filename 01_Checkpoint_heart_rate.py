"""
MTristan 
16/04/2022
"""

age = int(input("Please enter your age: "))
minRate = round((220 - age) * .65)
maxRate = round((220 - age) * .85)
print(f"When you exercise to strengthen your heart, you should \nkeep your heart rate between {minRate} and {maxRate} beats per minute.")
