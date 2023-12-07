from codrone_edu.drone import *
from fly_drone import *

# execute all necessary functions here
# run set_altitude() first and then fly_drone()

POWER = 40
THROTTLE = 20
DISTANCE = 60
ALTITUDE = 40


drone = Drone()
drone.pair()


fly_drone(drone, POWER, DISTANCE, ALTITUDE, THROTTLE)
