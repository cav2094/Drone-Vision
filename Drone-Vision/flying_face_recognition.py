# If you run into errors like - NotImplementedError: The operator
# https://github.com/ultralytics/ultralytics/issues/13152
# must be done in shell or before model libraries load
import os

try:
    os.environ["PYTORCH_ENABLE_MPS_FALLBACK"]
except KeyError:
    os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

import threading
from djitellopy import Tello
import cv2
from flight_routines import simple_flip
from video_processing import show_video_ml
from ultralytics import YOLO


def main():
    print("loading classifier")
    # face_classifier = cv2.CascadeClassifier(
    #     cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    # )

    yolo_classifer = YOLO("yolov8n.pt")
    print("complete")
    # Create a Tello object
    tello = Tello()

    # Connect to the Tello drone
    tello.connect()

    batter_percent = tello.get_battery()
    print(f"Battery: {batter_percent}%")
    x = threading.Thread(target=simple_flip, args=(tello,))
    x.start()
    show_video_ml(tello, yolo_classifer)

    # Disconnect from the drone
    tello.end()


if __name__ == "__main__":
    main()
