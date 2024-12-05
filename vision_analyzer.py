from google.cloud import vision
import cv2

class VisionAnalyzer:
    def __init__(self):
        """Initialize Google Cloud Vision client."""
        self.vision_client = vision.ImageAnnotatorClient()

    def analyze_image(self, image):
        """Analyze image using Google Cloud Vision API."""
        # Convert the image to bytes
        success, encoded_image = cv2.imencode('.jpg', image)
        if not success:
            raise Exception("Could not encode image")
            
        content = encoded_image.tobytes()
        image = vision.Image(content=content)

        # Perform detection
        response = self.vision_client.annotate_image({
            'image': image,
            'features': [
                {'type_': vision.Feature.Type.OBJECT_LOCALIZATION},
                {'type_': vision.Feature.Type.FACE_DETECTION},
                {'type_': vision.Feature.Type.LABEL_DETECTION},
            ]
        })

        return response