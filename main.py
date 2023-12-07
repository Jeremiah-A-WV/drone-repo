import time

from codrone_edu.drone import *
from fly_drone import *
from set_altitude import *

# execute all necessary functions here
# run set_altitude() first and then fly_drone()

POWER = 20
THROTTLE = 20
DISTANCE = 60
ALTITUDE = 50


drone = Drone()
drone.pair()
drone.set_initial_pressure()
time.sleep(2)
drone.takeoff()
set_altitude(drone, ALTITUDE, THROTTLE)
# drone.hover(3)
fly_drone(drone, POWER, DISTANCE)
