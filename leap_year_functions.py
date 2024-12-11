def is_leap(year):
    """
    Determines if a given year is a leap year.

    Arguments:
    year (int): The year to check.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    # A year is a leap year if:
    # 1. It is divisible by 4 AND
    # 2. It is not divisible by 100 OR it is divisible by 400.
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
 # Use Main Function 
if __name__ == '__main__':
    year = int(input("Enter the year: "))
    print(is_leap(year))
# Or directly done main function
"""
print(is_leap(2000))  # True (divisible by 400)
print(is_leap(1900))  # False (divisible by 100 but not 400)
print(is_leap(2400))  # True (divisible by 400)
print(is_leap(1990))  # False (not divisible by 4)
print(is_leap(2024))  # True (divisible by 4 but not 100)
"""   
