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
    #Let, Intial_Velocity=u, acceleration=a, time=t
    initial_velocity=float(input("Take your initial velocity in m/s: "))
    acceleration=float(input("Take your acceleration in m/s²: "))
    time=float(input("Take your time in second: "))
    final_velocity = initial_velocity+acceleration* time
    print("The final velocity is:",final_velocity,"m/s")
calc_final_velocity(8.0,7.6,9.0)
