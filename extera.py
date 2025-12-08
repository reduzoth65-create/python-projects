year = int(input("Enter a year: "))
if (year % 400 == 0):
    print(year, "is a leap year.")
elif (year % 100 == 0):
    print(year, "is NOT a leap year.")
elif (year % 4 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is NOT a leap year.")
