"""
MTristan 
24/04/2022
"""
from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()

if day_of_week == 0 or day_of_week >= 3:
    subtotal = float(input("Please enter the subtotal: "))
    taxes = subtotal * 0.06
    print(f"Sales tax amount: {taxes:.2f}")
    total = subtotal + taxes
    print(f"Total: {total:.2f}")
elif day_of_week == 1 or day_of_week == 2:
    subtotal = float(input("Please enter the subtotal: "))
    if subtotal >= 50:
        discount = subtotal * 0.10
        dSubtotal = subtotal - (subtotal * 0.10)
        print(f"Discount amount: {discount:.2f}")
        taxes = dSubtotal * 0.06
        print(f"Sales tax amount: {taxes:.2f}")
        total = dSubtotal + taxes
        print(f"Total: {total:.2f}")
    else:
        toDiscount = 50 - subtotal
        print(f"You need to add ${toDiscount:.2f} if you want to receive a discount")
        taxes = subtotal * 0.06
        print(f"Sales tax amount: {taxes:.2f}")
        total = subtotal + taxes
        print(f"Total: {total:.2f}")
