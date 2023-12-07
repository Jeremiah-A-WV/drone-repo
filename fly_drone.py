"""
This module contains a function that continuously calls a function
is_object_detected, which returns a True if a sensor detects an object
otherwise it returns False.  If is_object_detected returns a True, then
the avoid_object function is invoked to take action.


TEST TO ADJUST FORWARD_POWER TO YOUR LIKING
"""


def is_object_detected(drone, within_a_distance):
    """
    Returns a True if an object is less than or equal to
    the value passed to within_a_distance; otherwise False.
    """
    return drone.get_front_range() <= within_a_distance


def avoid_object(drone, forward_power):
    """
    Turns to the left and reads the front range sensor.
    Turns to the right and reads the front range sensor.
    If both left and right are blocked, then the drone goes back from where it came
    otherwise it goes right if the right side is not block.  If the right side is
    blocked, then the drone goes left if the left side is not blocked.
     # drone.get_front_range()
    # if drone.get_front_range() > within_a_distance:
    #     drone.turn_degree(90)
    #     if drone.get_front_range() > within_a_distance:
    #         drone.turn_degree(180)
    """
    # code does not move if distance > 150
    drone.set_pitch(0)
    drone.hover(1)
    drone.turn_left(90)
    left_turn = drone.get_front_range()
    drone.hover(1)
    drone.turn_right(180)
    right_turn = drone.get_front_range()
    drone.hover(1)
    if right_turn > 150:
        pass
    elif left_turn > 150:
        drone.turn_left(180)
    else:
        drone.turn_right(90)
    drone.hover(1)
    drone.set_pitch(forward_power)


def fly_drone(drone, forward_power, distance_threshold):
    # drone.takeoff()
    drone.set_pitch(forward_power)
    try:
        while True:
            drone.move()  # moves forward
            if is_object_detected(drone, distance_threshold):  # if an object is detected within 60 cms
                avoid_object(drone, forward_power)  # execute avoid_object() function
    except Exception as e:
        print(e)
        drone.set_pitch(0)  # set pitch to zero so the drone does not move
    finally:
        drone.land()  # when the try statement has concluded, land the drone
        drone.close()  # close the connection
