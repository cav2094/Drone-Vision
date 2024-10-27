"""
Real-time Video Processing with Machine Learning Models

This module provides functionality for real-time video processing using either
YOLO8 or cascade classifiers. It supports hardware acceleration via MPS (Apple Silicon)
when available.

Requirements:
    - OpenCV (cv2)
    - Ultralytics YOLO
    - PyTorch
    - Compatible video capture device
"""

import os
import cv2
import torch
from ultralytics import YOLO
from typing import Tuple, Optional

# Configure PyTorch MPS fallback before loading ML libraries
os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")


class VideoProcessor:
    """Handles video capture and processing using machine learning models."""

    def __init__(self, camera_index: int = 0) -> None:
        """
        Initialize the video processor.

        Args:
            camera_index: Index of the video capture device (default: 0)
        """
        self.device = "mps" if torch.backends.mps.is_available() else "cpu"
        self.camera_index = camera_index
        self.capture = None
        self.model = None

    def initialize_capture(self) -> bool:
        """
        Initialize the video capture device.

        Returns:
            bool: True if initialization successful, False otherwise
        """
        self.capture = cv2.VideoCapture(self.camera_index)
        return self.capture.isOpened()

    def load_yolo_model(self, model_path: str = "yolov8n.pt") -> None:
        """
        Load a YOLO model for object detection.

        Args:
            model_path: Path to the YOLO model weights
        """
        self.model = YOLO(model_path)
        print(f"Model loaded successfully. Using device: {self.device}")

    def process_frame_yolo8(self, frame: cv2.Mat) -> cv2.Mat:
        """
        Process a frame using YOLO object detection.

        Args:
            frame: Input frame from video capture

        Returns:
            cv2.Mat: Processed frame with annotations
        """
        results = self.model(frame, device=self.device, verbose=False)
        return results[0].plot()

    def process_frame_cascade(
        self, frame: cv2.Mat, classifier: cv2.CascadeClassifier
    ) -> cv2.Mat:
        """
        Process a frame using cascade classifier (e.g., face detection).

        Args:
            frame: Input frame from video capture
            classifier: OpenCV cascade classifier

        Returns:
            cv2.Mat: Processed frame with detections
        """
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detections = classifier.detectMultiScale(
            gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
        )

        # Draw rectangles around detected objects
        for x, y, w, h in detections:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

        # Add classifier information
        cv2.putText(
            frame,
            f"Classifier: {classifier}",
            (0, frame.shape[0] - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 0),
            2,
            cv2.LINE_AA,
        )

        return frame

    def read_frame(self) -> Tuple[bool, Optional[cv2.Mat]]:
        """
        Read a frame from the video capture device.

        Returns:
            Tuple containing success flag and frame (if successful)
        """
        if self.capture is None:
            return False, None
        return self.capture.read()

    def release(self) -> None:
        """Release video capture resources and close windows."""
        if self.capture is not None:
            self.capture.release()
        cv2.destroyAllWindows()


def main():
    """Main execution function for video processing demonstration."""
    processor = VideoProcessor()

    if not processor.initialize_capture():
        print("Error: Could not initialize video capture")
        return

    processor.load_yolo_model()

    print("Press 'q' to quit")

    try:
        while True:
            ret, frame = processor.read_frame()
            if ret:
                processed_frame = processor.process_frame_yolo8(frame)
                cv2.imshow("Video Processing", processed_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    except KeyboardInterrupt:
        print("\nProcessing interrupted by user")
    finally:
        processor.release()


if __name__ == "__main__":
    main()
