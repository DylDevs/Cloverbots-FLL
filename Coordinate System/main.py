# Imports
from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port
from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor
from pybricks.tools import wait, DataLog, StopWatch

# Variables
distances = {}

# Constants
wheel_diameter = 4.5
axle_track = 9.1

# Define the hub and any other motors or sensors
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=0, observe_channels=[])
left_motor = Motor(Port.A, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None)
right_motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None)
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
hub.imu.reset_heading(0) # Before running code, make sure the heading is reset

start_angle_position = 0
last_angle = 0
def SetDistances():
    # This will give an unpopulated dictionary that goes from 0-180 and -179 back to -1
    if distances == {}:
        for i in range(181): # Repeat 181 times to get a range of 0-180
            distances[i] = 0.0
            if i != 180: # We dont want 180 and -180
                distances[-i] = 0.0

    current_angle = hub.imu.heading()
    if current_angle != last_angle:
        last_angle = current_angle
        start_angle_position = 0

async def coordlog(lgname):
    datlog = DataLog("time", "gyro", "distance", name=lgname, timestamp=True, extension=".csv")
    while True:
        x = hub.imu.heading()
        time = StopWatch.time()
        if not x == hub.imu.heading():
            datlog.log(time, hub.imu.heading(), robot.distance())
            StopWatch.reset()