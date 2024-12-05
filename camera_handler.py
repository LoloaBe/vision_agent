import cv2
import numpy as np

class CameraHandler:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index

    def capture_frame(self):
        """Capture a frame from the webcam."""
        cap = cv2.VideoCapture(self.camera_index)
        ret, frame = cap.read()
        cap.release()
        
        if not ret:
            raise Exception("Could not capture frame from camera")
            
        return frame

    def draw_detections(self, image, response):
        """Draw bounding boxes and labels on the image."""
        image_with_detections = image.copy()
        
        # Draw object detections
        for obj in response.localized_object_annotations:
            vertices = [(int(vertex.x * image.shape[1]), int(vertex.y * image.shape[0])) 
                       for vertex in obj.bounding_poly.normalized_vertices]
            
            # Draw bounding box
            for i in range(4):
                cv2.line(image_with_detections, vertices[i], vertices[(i+1)%4], (0, 255, 0), 2)
            
            # Draw label
            cv2.putText(image_with_detections, 
                       f"{obj.name}: {obj.score:.2f}",
                       (vertices[0][0], vertices[0][1] - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Draw face detections
        for face in response.face_annotations:
            vertices = [(int(vertex.x), int(vertex.y)) 
                       for vertex in face.bounding_poly.vertices]
            
            # Draw face box in red
            for i in range(4):
                cv2.line(image_with_detections, vertices[i], vertices[(i+1)%4], (0, 0, 255), 2)

        return image_with_detections