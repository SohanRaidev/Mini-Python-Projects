
age = input("Enter your current age: ")
expage = input("Enter the age you expect to live: ")


current_age = int(age)
expected_age = int(expage)

remaining_years = expected_age - current_age
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365

print(f"You have {remaining_years} years, {remaining_months} months, {remaining_weeks} weeks, and {remaining_days} days left to live.")
