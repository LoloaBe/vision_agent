import cv2
import numpy as np
import time
from datetime import datetime

class CameraHandler:
    def __init__(self, camera_index=0):
        """Initialize the camera handler.
        
        Args:
            camera_index (int): Index of the camera to use (default is 0 for built-in webcam)
        """
        self.camera_index = camera_index
        self.cap = None

    def initialize_camera(self):
        """Initialize the camera if not already initialized."""
        if self.cap is None:
            self.cap = cv2.VideoCapture(self.camera_index)
            # Allow the camera sensor to warm up
            time.sleep(0.1)
            
            # Set camera properties for better quality
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            self.cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)
            self.cap.set(cv2.CAP_PROP_BRIGHTNESS, 150)

    def capture_frame(self):
        """Capture a frame from the webcam.
        
        Returns:
            numpy.ndarray: The captured frame
        
        Raises:
            Exception: If frame cannot be captured
        """
        if self.cap is None:
            self.initialize_camera()
        
        ret, frame = self.cap.read()
        
        if not ret:
            # If frame capture failed, try to reinitialize the camera
            self.release_camera()
            self.initialize_camera()
            ret, frame = self.cap.read()
            if not ret:
                raise Exception("Could not capture frame from camera")
            
        return frame

    def draw_detections(self, image, response):
        """Draw bounding boxes and labels on the image.
        
        Args:
            image (numpy.ndarray): The original image
            response: The detection response from Vision API
        
        Returns:
            numpy.ndarray: Image with detections drawn
        """
        image_with_detections = image.copy()
        
        # Draw object detections
        for obj in response.localized_object_annotations:
            vertices = [(int(vertex.x * image.shape[1]), int(vertex.y * image.shape[0])) 
                       for vertex in obj.bounding_poly.normalized_vertices]
            
            # Draw bounding box
            for i in range(4):
                cv2.line(image_with_detections, 
                        vertices[i], 
                        vertices[(i+1)%4], 
                        (0, 255, 0),  # Green color
                        2)  # Line thickness
            
            # Draw label with score
            label = f"{obj.name}: {obj.score:.2f}"
            cv2.putText(image_with_detections, 
                       label,
                       (vertices[0][0], vertices[0][1] - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 
                       0.5,  # Font scale
                       (0, 255, 0),  # Green color
                       2)  # Line thickness

        # Draw face detections
        for face in response.face_annotations:
            vertices = [(int(vertex.x), int(vertex.y)) 
                       for vertex in face.bounding_poly.vertices]
            
            # Draw face box in red
            for i in range(4):
                cv2.line(image_with_detections, 
                        vertices[i], 
                        vertices[(i+1)%4], 
                        (0, 0, 255),  # Red color
                        2)  # Line thickness
            
            # Add confidence score for face
            confidence = f"Confidence: {face.detection_confidence:.2f}"
            cv2.putText(image_with_detections,
                       confidence,
                       (vertices[0][0], vertices[0][1] - 10),
                       cv2.FONT_HERSHEY_SIMPLEX,
                       0.5,
                       (0, 0, 255),
                       2)

        # Add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(image_with_detections,
                   timestamp,
                   (10, 30),  # Position in top-left corner
                   cv2.FONT_HERSHEY_SIMPLEX,
                   1,
                   (255, 255, 255),  # White color
                   2)

        return image_with_detections

    def release_camera(self):
        """Release the camera resources."""
        if self.cap is not None:
            self.cap.release()
            self.cap = None

    def __del__(self):
        """Destructor to ensure camera is released."""
        self.release_camera()