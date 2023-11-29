from codrone_edu.drone import *
# import time

THROTTLE_POWER = 30


def set_altitude(altitude):
    height = drone.height_from_pressure()

    if altitude <= height:
        sign = -1
    else:
        sign = 1

    drone.set_throttle(sign * THROTTLE_POWER)
    drone.move()

    while sign * altitude > sign * height:
        print("Current height is " + height)
        # UPDATE HEIGHT OF DRONE

    drone.set_throttle(0)


drone = Drone()
drone.pair()
drone.set_initial_pressure()
try:
    drone.takeoff()
    drone.hover(2)
    set_altitude(40)
    print('Final Height =', drone.height_from_pressure())
    drone.hover(2)
    set_altitude(150)
    print('Final Height =', drone.height_from_pressure())
    drone.hover(3)
except Exception as e:
    print(e)
drone.land()
drone.close()
