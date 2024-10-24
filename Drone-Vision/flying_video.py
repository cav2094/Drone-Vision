import threading
from djitellopy import Tello
from flight_routines import simple_flip
from video_processing import show_video


def main():
    # Create a Tello object
    tello = Tello()

    # Connect to the Tello drone
    tello.connect()

    batter_percent = tello.get_battery()
    print(f"Battery: {batter_percent}%")
    x = threading.Thread(target=show_video, args=(tello,))
    x.start()
    simple_flip(tello)

    # Disconnect from the drone
    tello.end()


if __name__ == "__main__":
    main()
