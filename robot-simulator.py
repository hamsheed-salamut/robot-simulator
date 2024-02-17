import math

# Dictionary mapping orientation to movement in (dx, dy) format
movement_map = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

def move_robot(commands, initial_position):
    x, y, orientation = initial_position

    for command in commands:
        if command == 'F':
            dx, dy = movement_map[orientation]
            x = max(0, min(x + dx, 9))
            y = max(0, min(y + dy, 9))
        elif command == 'B':
            dx, dy = movement_map[orientation]
            x = max(0, min(x - dx, 9))
            y = max(0, min(y - dy, 9))
        elif command == 'L':
            orientation = rotate_orientation(orientation, True)
        elif command == 'R':
            orientation = rotate_orientation(orientation, False)

    return x, y, orientation

def rotate_orientation(current_orientation, turn_left):
    orientations = ['N', 'E', 'S', 'W']
    current_index = orientations.index(current_orientation)
    new_index = (current_index + 3) % 4 if turn_left else (current_index + 1) % 4
    return orientations[new_index]

def main():
    # Input handling
    initial_position_input = input("Enter initial position (x y orientation): ").split()
    x, y, orientation = int(initial_position_input[0]), int(initial_position_input[1]), initial_position_input[2]

    command_input = input("Enter commands (F for forward, B for backward, L for turn left, R for turn right): ")
    commands = list(command_input)

    # Moving the robot
    final_position = move_robot(commands, (x, y, orientation))

    # Output
    print(f"Final position of the robot: {final_position[0]} {final_position[1]} {final_position[2]}")

if __name__ == "__main__":
    main()