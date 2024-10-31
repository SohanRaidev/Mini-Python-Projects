import math

# Input the total bill amount
bill = float(input("Enter the total bill amount: Rs "))

# Input the desired tip percentage
tip_percentage = float(input("Enter the tip percentage you'd like to give: "))

# Input the number of people to split the bill
people = int(input("How many people are splitting the bill? "))

# Calculate the total tip
tip_amount = bill * (tip_percentage / 100)

# Calculate the total bill including tip
total_bill = bill + tip_amount

# Calculate each person's share
per_person = total_bill / people

print(f"\nBill Summary:\n")
print(f"Total Bill (before tip): Rs {bill:.2f}")
print(f"Tip Percentage: {tip_percentage}%")
print(f"Tip Amount: Rs {tip_amount:.2f}")
print(f"Total Bill (with tip): Rs {total_bill:.2f}")
print(f"Each person owes: Rs {per_person:.2f} (split among {people} people)")
