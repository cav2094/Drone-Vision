import time

"""
Flight routines for Tello drone
Simple flip demonstration routine with safety delays
"""


def simple_flip(tello):
    # Initial safety delay
    time.sleep(3)

    print("Takeoff initiated.")
    # Take off to default height
    tello.takeoff()

    # Wait for stabilization with status checks
    for _ in range(3):
        time.sleep(1)
        try:
            battery = tello.get_battery()
            print(f"Battery level: {battery}%")
        except:
            print("Could not get battery reading")

    # Execute flip maneuver
    print("Executing right flip...")
    tello.flip_right()

    # Post-flip stabilization delay
    time.sleep(2)

    # Safe landing
    print("Landing sequence initiated.")
    tello.land()

    # Confirmation delay
    time.sleep(3)
    print("Flight routine completed.")

def simple_scan(tello):
    # Initial safety delay
    time.sleep(3)

    print("Takeoff initiated.")
    # Take off to default height
    tello.takeoff()

    # Wait for stabilization with status checks
    for _ in range(3):
        time.sleep(1)
        try:
            battery = tello.get_battery()
            print(f"Battery level: {battery}%")
        except:
            print("Could not get battery reading")

    # Execute grid scan maneuver
    print("Executing grid scan...")
    grid_routine(tello, 20, 3)
    


    # Post-flip stabilization delay
    time.sleep(2)

    # Safe landing
    print("Landing sequence initiated.")
    tello.land()

    # Confirmation delay
    time.sleep(3)
    print("Flight routine completed.")

def grid_routine(tello, x, y):
    for i in range(y):
        tello.move_forward(x)

        rotate_clockwise(90)
        tello.move_forward(x)
        rotate_clockwise(90)

        tello.move_forward(x)

        rotate_counter_clockwise(90)
        tello.move_forward(x)
        rotate_counter_clockwise(90)