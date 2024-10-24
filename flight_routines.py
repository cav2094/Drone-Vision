import time

"""
Flight routines
"""


def simple_flip(tello):
    time.sleep(3)
    print("Takeoff.")
    # Take off to a certain height
    tello.takeoff()

    for _ in range(3):
        time.sleep(1)  # Wait for stabilization
    # ValueError: invalid literal for int() with base 10: '100.0'
    # speed = tello.query_speed()
    # print(f"Speed is now {speed} (cm/s)")

    # Do a flip (replace with desired flip command if needed)
    print("Executing a flip.")
    tello.flip_right()
    time.sleep(1)  # Wait for completion

    # Land slowly
    print("Landing.")
    tello.land()
    time.sleep(3)  # Wait for landing confirmation
