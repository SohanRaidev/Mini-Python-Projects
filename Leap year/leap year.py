
year = int(input("Enter a year to check if it is a leap year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"\n{year} is a leap year.\n")
else:
    print(f"\n{year} is not a leap year.\n")
