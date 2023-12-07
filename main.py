from codrone_edu.drone import *
from fly_drone import *
from set_altitude import *

# execute all necessary functions here
# run set_altitude() first and then fly_drone()

POWER = 15
THROTTLE = 20
DISTANCE = 60
ALTITUDE = 40


drone = Drone()
drone.pair()

drone.set_initial_pressure()
drone.takeoff()

set_altitude(drone, ALTITUDE, THROTTLE)
# drone.hover(3)
fly_drone(drone, POWER, DISTANCE)
