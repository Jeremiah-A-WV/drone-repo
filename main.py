from codrone_edu.drone import *
from fly_drone import *
from set_altitude import *

# execute all necessary functions here
# run set_altitude() first and then fly_drone()

POWER = 40
THROTTLE = 20
DISTANCE = 60
ALTITUDE = 40


drone = Drone()
drone.pair()

set_altitude(drone, ALTITUDE, THROTTLE)
# drone.hover(3)
drone.takeoff()
fly_drone(drone, POWER, DISTANCE)
