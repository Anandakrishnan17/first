units_consumed=int(input("Enter the unit consumed:"))

if units_consumed < 100:
    price_per_unit = 0.50
elif 100 <= units_consumed <= 200:
    price_per_unit = 0.50 if units_consumed <= 100 else 0.75
elif 200 <= units_consumed <= 300:
    price_per_unit = 0.50 if units_consumed <= 100 else 0.75 if units_consumed <= 200 else 1.0
else:
    price_per_unit = 0.50 if units_consumed <= 100 else 0.75 if units_consumed <= 200 else 1.0 if units_consumed <= 300 else 2.0
    
total_bill = units_consumed * price_per_unit
print("Total bill:",total_bill)