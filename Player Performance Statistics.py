minute = float(input("How many minutes the player was on the field: "))
goal = int(input("How many goals the player scored: "))
total_shoot = int(input("How many times the player tried to shoot: "))
shoots_toward_the_target = int(input("How many shots actually went towards the goal: "))
distance = float(input("How many kilometers the player ran : "))


shot_accuracy = (shoots_toward_the_target/total_shoot)*100 # Shot accuracy
goal_scoringrate = (goal/total_shoot)*100 # Goal scoring rate 
average_speed = (distance/minute)  # Average speed in kilometer per minute

actual_averagespeed = (average_speed *1000)/60   # Average spees in meter per second

"""
I didn't use if else statement because you 
said that this is our first assignemnt, so try except structure 
are not needed.
"""

'''

print("The shot accuracy is: ", shot_accuracy, "%")
print("The Goal scoring rate is: ", goal_scoringrate,"%")
print("The average speed of player is: ", average_speed , "km/m")
print("The average speed of player is: ", actual_averagespeed,"m/s")

'''
print("\nPlayer Performance Statistics:")

print(f"The shot accuracy is : {shot_accuracy:.2F} %")
print(f"The goal scoring rate is : {goal_scoringrate:.3F} %")
print(f"The average speed is : {average_speed:.3F} km/m")
print(f"The average speed in meter per second is : {actual_averagespeed:.2F} m/s")
