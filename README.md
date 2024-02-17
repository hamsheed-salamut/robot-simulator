# Robot Movement Simulator
[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

This Python script simulates the movement of a robot in a grid-based environment. The robot can move forward, backward, turn left, and turn right based on user commands.

## Prerequisites
Before running the script, ensure you have Python installed on your system. You can download and install Python from the [official Python website](https://www.python.org/downloads/). Follow the installation instructions provided for your operating system.

## Features
- Moves the robot in a 2D grid environment.
- Supports commands for moving forward, backward, turning left, and turning right.
- Prevents the robot from moving beyond the boundaries of the grid (10x10).
- Accepts user input for initial position and movement commands.
- Outputs the final position of the robot after executing the commands.

## Usage
1. Clone or download the `robot_movement.py` script to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `robot_movement.py` script is located.
4. Run the script by entering the following command:
 
    ```powershell
    python robot_movement.py
    ```
5. Follow the on-screen instructions to provide the initial position and movement commands for the robot.
6. View the final position of the robot displayed on the console.

## Example
```
Enter initial position (x y orientation): 0 0 N
Enter commands (F for forward, B for backward, L for turn left, R for turn right): F R F L B
Final position of the robot: 1 0 N

```

## Code Highlights
This block defines a dictionary named `movement_map`. It maps each cardinal direction ('N', 'S', 'E', 'W') to a tuple representing the change in coordinates (dx, dy) associated with moving in that direction.

```python
# Dictionary mapping orientation to movement in (dx, dy) format
movement_map = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}
```

This block defines the `move_robot` function. It iterates through each command in the commands list and updates the position of the robot accordingly. If the command is 'F' (forward) or 'B' (backward), it calculates the new coordinates while ensuring the robot stays within the grid bounds. If the command is 'L' (turn left) or 'R' (turn right), it rotates the orientation of the robot.
```python
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
```

This block defines the `rotate_orientation` function, which rotates the orientation of the robot based on the current orientation and the direction of rotation (left or right).
```python
def rotate_orientation(current_orientation, turn_left):
    orientations = ['N', 'E', 'S', 'W']
    current_index = orientations.index(current_orientation)
    new_index = (current_index - 1) % 4 if turn_left else (current_index + 1) % 4
    return orientations[new_index]

```

This block defines the main function, which is the entry point of the script. It prompts the user to enter the initial position and movement commands for the robot, calls the `move_robot` function to determine the final position of the robot, and prints the final position as output.

The `if __name__ == "__main__":` block ensures that the main function is executed only when the script is run directly.

```python
def main():
    # Prompt input for initial position
    initial_position_input = input("Enter initial position (x y orientation): ").split()
    x, y, orientation = int(initial_position_input[0]), int(initial_position_input[1]), initial_position_input[2].upper()

    # Prompt input for commands
    command_input = input("Enter commands (F for forward, B for backward, L for turn left, R for turn right): ")
    commands = list(command_input.upper())

    # Moving the robot
    final_position = move_robot(commands, (x, y, orientation))

    # Output
    print(f"Final position of the robot: {final_position[0]} {final_position[1]} {final_position[2]}")

if __name__ == "__main__":
    main()
```
