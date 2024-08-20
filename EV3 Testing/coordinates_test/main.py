#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
import math

# Initialize the EV3 brick and motors
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Robot parameters (may require calibration)
WHEEL_DIAMETER = 4.5  # cm
AXLE_TRACK = 9.1  # cm, distance between the two wheels

# Initialize the DriveBase with your motors
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK)
drive_base.settings(200, 200, 200, 200) 

# Initial position and heading
x, y = 0, 0  # Starting at origin
heading = 0  # Facing straight ahead

# Function to calculate distance from motor rotations
def calculate_distance(degrees):
    return (degrees / 360) * math.pi * WHEEL_DIAMETER

# Function to update position and heading based on motor encoder readings
def update_position():
    global x, y, heading
    
    # Get the rotation angle of each motor
    left_degrees = left_motor.angle()
    right_degrees = right_motor.angle()
    
    # Calculate the distance each wheel has traveled
    left_distance = calculate_distance(left_degrees)
    right_distance = calculate_distance(right_degrees)
    
    # Calculate the change in heading (in radians)
    angle_change = (right_distance - left_distance) / AXLE_TRACK
    
    # Update heading and round to avoid floating-point issues
    heading += angle_change
    heading = round(heading, 5)  # Round to avoid floating-point inaccuracies
    
    # Calculate the average distance traveled
    distance = (left_distance + right_distance) / 2.0
    
    # Update x and y position based on the new heading
    x += distance * math.cos(heading)
    y += distance * math.sin(heading)
    
    return x, y, math.degrees(heading)  # Return heading in degrees

def PrintPosition():
    new_x, new_y, new_heading = update_position()
    print("New Position: x =" + str(new_x) + " cm, y = " + str(new_y) + " cm, heading = " + str(new_heading) + " degrees")


# Reset motor encoders to start fresh
left_motor.reset_angle(0)
right_motor.reset_angle(0)
PrintPosition()

# Example movement: Move forward for 50 mm (0.05 meter)
drive_base.straight(50)
PrintPosition()

# Calibrate turn by trial and error
drive_base.turn(-90)
PrintPosition()

# Move forward again
drive_base.straight(50)
PrintPosition()
