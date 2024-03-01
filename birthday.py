def days_since_birthday(birthday):
    # Extract the year from the birthday
    year = int(birthday.split('-')[2])

    # Assume a current year, manually set
    current_year = 2024

    days = 0
    # Loop through each year from the year after the birth year up to the year before the current year
    for y in range(year + 1, current_year):
        # Check if the year is a leap year
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            days += 366  # Add days for a leap year
        else:
            days += 365  # Add days for a non-leap year

    return days


# Example usage
birthday = "11-11-2004"
days_passed = days_since_birthday(birthday)
print(days_passed)
