def display_year_calendar():
    """
    Displays the calendar for an entire year.
    """
    year = int(input("Enter the year: "))
    cal = calendar.TextCalendar(calendar.SUNDAY)  # Start the week on Sunday
    print(cal.formatyear(year, 2, 1, 1, 4)) #formatyear(year, width, spacing, c, m) generates a string representation of the calendar for the entire year.
#year: The year to display.
#width=2: Width of each date column.
#spacing=1: Space between months.
#c=1: Number of rows per month.
#m=4: Number of months per row.

display_year_calendar()
