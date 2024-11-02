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
  if time < 0:
    return None
  else:
    displacement = initial_velocity * time + 0.5 * acceleration * time ** 2
    print("The displacement (s) is:", displacement, "m")
    
if __name__=='__main__':
   initial_velocity = float(input("Enter initial velocity (u) in m/s: "))
   acceleration = float(input("Enter acceleration (a) in m/s²: "))
   time = float(input("Enter time (t) in second: "))
   print()
   calc_displacement(initial_velocity, acceleration, time)
 


    



