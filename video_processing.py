import cv2
from ml_processing import process_frame_yolo8
from djitellopy import Tello
"""
Just video processing
"""


def show_video_ml(tello, classifier):
    # Start the video stream
    print("Tuning on the stream")
    tello.streamon()

    # Create a VideoCapture object using the Tello's video stream address
    print("creating VideoCapture object")
    cap = cv2.VideoCapture(tello.get_udp_video_address())

    # Read and display the video stream
    print("Starting stream...")
    try:
        count = 0
        while True:
            ret, frame = cap.read()
            if ret:
                if count % 3 == 0:
                    frame = process_frame_yolo8(frame, classifier)
                    cv2.imshow("Tello Video", frame)
                    count = 0
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            count+=1
    except Exception as e:
        print("Caught Exception ", e)

    # Clean up
    cv2.destroyAllWindows()
    cap.release()
    tello.streamoff()


def show_video(tello):
    # Start the video stream
    print("Tuning on the stream")
    tello.streamon()

    # Create a VideoCapture object using the Tello's video stream address
    print("creating VideoCapture object")
    cap = cv2.VideoCapture(tello.get_udp_video_address())

    # Read and display the video stream
    print("Starting stream...")
    try:
        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imshow("Tello Video", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    except Exception as e:
        print("Caught Exception ", e)

    # Clean up
    cv2.destroyAllWindows()
    cap.release()
    tello.streamoff()
