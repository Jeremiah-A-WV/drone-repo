def set_altitude(drone, altitude, throttle):
    height = drone.height_from_pressure()

    if altitude <= height:
        sign = -1
    else:
        sign = 1

    drone.set_throttle(sign * throttle)
    drone.move()

    while sign * altitude > sign * height:
        print("Current height is " + height)
        # UPDATE HEIGHT OF DRONE

    drone.set_throttle(0)


def read_final_height(drone, altitude, throttle):

    drone.set_initial_pressure()
    try:
        drone.hover(2)
        set_altitude(drone, altitude, throttle)
        print('Final Height =', drone.height_from_pressure())
        drone.hover(2)
    except Exception as e:
        print(e)
    finally:
        drone.land()
        drone.close()
