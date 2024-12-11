import calendar #Imports Python's built-in calendar module, which provides methods to work with calendars and dates.
def display_calender(): #Defines a function named display_calender.
  year = int(input("Enter the year: "))
  month = int(input("Enter the month: "))
  cal = calendar.TextCalendar(calendar.WEDNESDAY)
  #Creates a TextCalendar object named cal from the calendar module.
  #The calendar.WEDNESDAY parameter sets the first day of the week in the calendar to Wednesday.
  #The TextCalendar class generates simple, text-based calendars.
  cal.prmonth(year, month)
  #Calls the prmonth() method of the TextCalendar object (cal).
  #This method prints the calendar for the specified year and month to the console.
  print(cal)
display_calender()
