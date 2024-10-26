"""
Tello Drone Control Script

This module provides basic control functionality for the DJI Tello drone,
including battery status checking, video streaming, and simple flight routines.

Dependencies:
    - djitellopy
    - threading
"""

import threading
import logging
from typing import Optional
from djitellopy import Tello
from flight_routines import simple_flip
from video_processing import show_video


class DroneConnectionError(Exception):
    """Custom exception for drone connection failures."""

    pass


def initialize_drone() -> Optional[Tello]:
    """
    Initialize and connect to the Tello drone.

    Returns:
        Tello: Connected Tello drone object if successful.

    Raises:
        DroneConnectionError: If connection to drone fails.
    """
    try:
        drone = Tello()
        drone.connect()
        return drone
    except Exception as e:
        logging.error(f"Failed to connect to Tello drone: {str(e)}")
        raise DroneConnectionError(
            "Could not establish connection with the drone"
        ) from e


def check_battery(drone: Tello, min_battery_level: int = 10) -> bool:
    """
    Check drone battery level and verify it's above minimum threshold.

    Args:
        drone: Connected Tello drone object
        min_battery_level: Minimum acceptable battery percentage (default: 10)

    Returns:
        bool: True if battery level is acceptable, False otherwise
    """
    try:
        battery_level = drone.get_battery()
        logging.info(f"Battery Level: {battery_level}%")

        if battery_level <= min_battery_level:
            logging.warning(f"Low battery warning: {battery_level}%")
            return False
        return True
    except Exception as e:
        logging.error(f"Failed to check battery level: {str(e)}")
        return False


def start_video_stream(drone: Tello) -> threading.Thread:
    """
    Initialize and start the video stream in a separate thread.

    Args:
        drone: Connected Tello drone object

    Returns:
        threading.Thread: Video streaming thread object
    """
    video_thread = threading.Thread(
        target=show_video, args=(drone,), name="VideoStream"
    )
    video_thread.daemon = True  # Ensure thread terminates with main program
    video_thread.start()
    return video_thread


def main() -> None:
    """
    Main execution function that coordinates drone operations.
    Handles initialization, flight routines, and cleanup.
    """
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    try:
        # Initialize and connect to drone
        drone = initialize_drone()

        # Verify battery level is sufficient
        if not check_battery(drone):
            logging.error("Insufficient battery level to proceed")
            return

        # Start video stream
        video_thread = start_video_stream(drone)

        # Execute flight routine
        try:
            simple_flip(drone)
        except Exception as e:
            logging.error(f"Flight routine failed: {str(e)}")

        # Wait for video thread to complete
        video_thread.join(timeout=5.0)

    except DroneConnectionError as e:
        logging.error(f"Drone connection error: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
    finally:
        if "drone" in locals():
            try:
                drone.end()
                logging.info("Drone connection terminated successfully")
            except Exception as e:
                logging.error(f"Error disconnecting from drone: {str(e)}")


if __name__ == "__main__":
    main()
