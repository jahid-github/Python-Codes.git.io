# This instruction from my teacher Date: 28/10/24
# Displacement Calculator
#def calc_displacement(initial_velocity, acceleration, time):
#Calculate displacement using s = ut + (1/2)at²
#Parameters:
    #initial_velocity (float): Initial velocity in m/s
    #acceleration (float): Acceleration in m/s²
    #time (float): Time in seconds
    
    #Returns:
    #float: Displacement in meters
    #None: If time is negative
    
# My code here
def calc_displacement(initial_velocity, acceleration, time):
#Let, Intial_Velocity=u, acceleration=a, time=t
 
 intial_velocity=float(input("Take your initial velocity in m/s: "))
 acceleration=float(input("Take your acceleration in m/s²: "))
 time=float(input("Take your time in second: "))
 displacement = initial_velocity * time + 0.5 * acceleration * time ** 2
 print("The displacement is:", displacement, "m")
 if time < 0:
      print("Error: Time cannot be negative.")
 return None
calc_displacement(8.0,7.6,9.0)
