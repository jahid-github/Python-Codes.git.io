# This instruction from my teacher Date: 28/10/24
# Basic Motion Calculator
#def calc_final_velocity(initial_velocity, acceleration, time):

#Calculate final velocity using v = u + at
    
#Parameters:
    #initial_velocity (float): Initial velocity in m/s
    #acceleration (float): Acceleration in m/s²
    #time (float): Time in seconds
    
    #Returns:
    #float: Final velocity in m/s

    # My code here
def calc_final_velocity(initial_velocity, acceleration, time):
    final_velocity = initial_velocity + (acceleration * time)
    rounded_number=round(final_velocity,2)
    print("The final velocity (v) is:",rounded_number,"m/s")

if __name__=='__main__':
   initial_velocity = float(input("Enter initial velocity (u) in m/s: "))
   acceleration = float(input("Enter acceleration (a) in m/s²: "))
   time = float(input("Enter time (t) in second: "))
   print()
   calc_final_velocity(initial_velocity, acceleration, time)

#SampleInput
#Enter initial velocity (u) in m/s: 20
#Enter acceleration (a) in m/s²: -5
#Enter time (t) in second: 4
#SampleOutput
#The final velocity (v) is: 0.0 m/s
