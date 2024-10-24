# If you run into errors like - NotImplementedError: The operator
# https://github.com/ultralytics/ultralytics/issues/13152
# must be done in shell or before model libraries load
import os

try:
    os.environ["PYTORCH_ENABLE_MPS_FALLBACK"]
except KeyError:
    os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

import cv2
from ultralytics import YOLO
import torch

"""
machine learning processing of video frames
"""

# run
# conda env config vars set PYTORCH_ENABLE_MPS_FALLBACK=1
# conda activate drone-ai

DEVICE = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Usinng backend {DEVICE=}")
# MP1 Pro CPU -
#   1.6ms preprocess, 187.2ms inference, 0.7ms postprocess
# MP1 Pro MPS (w/ CPU fallback) -
#   2.1ms preprocess, 19.9ms inference, 7.2ms postprocess

"""
Processes fram with bounding box classifier
"""


def process_frame_bb(frame, classifier):
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    updated_frame = classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )

    for x, y, w, h in updated_frame:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

    cv2.putText(
        frame,
        f"RUNNING: {classifier=}",
        (
            0,
            frame.shape[0] - 20,
        ),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 0),
        2,
        cv2.LINE_AA,
        bottomLeftOrigin=False,
    )

    # print(frame.shape)
    return frame


def process_frame_yolo8(frame, model):

    results = model(frame, device=DEVICE, verbose = False)  # list of Results objects
    annotated_frame = results[0].plot()

    return annotated_frame


"""
For testing purposes read from the webcam
"""


def main():

    print("loading classifier...", end="")
    # Load OpenCV face detector
    # face_classifier = cv2.CascadeClassifier(
    #    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    # )

    # Load a pretrained YOLOv8n model
    model = YOLO("yolov8n.pt")

    print("complete")

    # define a video capture object
    vid = cv2.VideoCapture(0)

    while True:

        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        if ret:
            frame = process_frame_yolo8(frame, model)

            # Display the resulting frame
            cv2.imshow("frame", frame)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
