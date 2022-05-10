"""
MTristan 
24/04/2022
"""
import math

items = int(input("Enter the number of items: "))
itemsXbox = int(input("Enter the number of items per box: "))
boxes = math.ceil(items/itemsXbox)


print(f"For {items} items, packing {itemsXbox} items in each box, you will need {boxes} boxes")
