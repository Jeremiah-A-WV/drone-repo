def set_altitude(drone, altitude, throttle):
    current_altitude = drone.height_from_pressure()
    if altitude <= current_altitude:
        sign = -1
    else:
        sign = 1

    drone.set_throttle(sign * throttle)

    drone.move()
    while sign * altitude > sign * current_altitude:
        current_altitude = drone.height_from_pressure()
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
