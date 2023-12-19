# Get the charge for the food from the user
food_charge = float(input("Enter the charge for the food: $"))

# Calculate the tip (18% of the food charge)
tip_percentage = 18
tip_amount = (tip_percentage / 100) * food_charge

# Calculate the sales tax (7% of the food charge)
sales_tax_percentage = 7
sales_tax_amount = (sales_tax_percentage / 100) * food_charge

# Calculate the grand total
grand_total = food_charge + tip_amount + sales_tax_amount

# Display the results
print(f"\nTip = ${tip_amount:.2f}")
print(f"Sales tax = ${sales_tax_amount:.2f}")
print(f"Grand total = ${grand_total:.2f}")
