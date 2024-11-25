"""Robotic Path Planning Functions Assignment"""
#Function 1: Basic Movement Calculation

def calculate_movement(current_position: tuple[int, int], direction: str, distance: int) -> tuple[int, int]:
    """
    Input Parameters:  Calculate the next position of the robot based on current position, direction, and distance.
    """
    x, y=current_position
    move_map={"N": (0, distance), "S": (0, -distance), "E": (distance, 0), "W": (-distance, 0)}
    dx,dy=move_map.get(direction,(0,0))
    
    if (dx, dy)==(0, 0):
       return ValueError("Invalid direction. Use 'N', 'S, 'E', or 'W'.")
    x += dx
    y += dy
    
    # Ensure the new position is within grid boundaries (0-9 x 0-9)
    x=max(0, min(9,x))
    y=max(0, min(9,y))
    return(x, y)
# Test cases
print(calculate_movement((0, 0), 'N', 3))  # Expected: (0, 3)
print(calculate_movement((5, 5), 'W', 2))  # Expected: (3, 5)
print(calculate_movement((3, 2), 'S', 5))  
print(calculate_movement((7, 2), 'E', 2))
#Function 2: Path Generation Function

def generate_path(start_position: tuple, target_position: tuple) -> list:
    """
    Generate a sequence of movements to reach the target position from the start position using Manhattan distance.
    """
    current_position=start_position
    target_x, target_y=target_position
    path=[]
     
    # Move horizontally first (East or West) using a dictionary to avoid if statements
    horizontal_distance = target_x - current_position[0]
    direction = 'E' if horizontal_distance > 0 else 'W'
    if horizontal_distance != 0:
        path.append((direction, abs(horizontal_distance)))

    # Move vertically (North or South) using a dictionary
    vertical_distance = target_y - current_position[1]
    direction = 'N' if vertical_distance > 0 else 'S'
    if vertical_distance != 0:
        path.append((direction, abs(vertical_distance)))
    return path
# Test cases
print(generate_path((0, 0), (3, 4)))  # Expected: [('E', 3), ('N', 4)]

#Function 3: Obstacle Avoidance Function

def navigate_with_obstacles(start_position: tuple, target_position: tuple, obstacles: list) ->list:
    """
    Navigate from start to target position while checking for obstacles in the path.
    If any obstacle is found on the path, return None.
    """
    path=generate_path(start_position, target_position)
    current_position=start_position
    
    # Using a dictionary to avoid if statements for movement
    direction_map={"N": (0, 1), "S": (0, -1), "E":(1, 0), "W": (-1, 0)}
    
    # Check each movement in the path
    for direction, distance in path:
        dx, dy = direction_map[direction]
        for i in range (distance):
           current_position=(current_position[0]+dx, current_position[1]+dy)
           #Check if the current position is an obstacle
           if current_position in obstacles:
               return None
    return path 

# Test cases
obstacles = [(2, 2), (2, 3)]
print(navigate_with_obstacles((0, 0), (5, 5), obstacles))  # Expected: [('E', 5), ('N', 5)]

obstacles = [(2, 0), (2, 3)]
print(navigate_with_obstacles((0, 0), (5, 5), obstacles))  # Expected: None
