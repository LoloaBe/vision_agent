import cv2
import time
from datetime import datetime

class SecurityAgent:
    def __init__(self, camera_handler, vision_analyzer, report_generator):
        self.camera_handler = camera_handler
        self.vision_analyzer = vision_analyzer
        self.report_generator = report_generator

    def monitor(self, interval=5):
        """Continuous monitoring with specified interval."""
        print("Starting security monitoring. Press Ctrl+C to stop.")
        
        try:
            while True:
                frame = self.camera_handler.capture_frame()
                response = self.vision_analyzer.analyze_image(frame)
                frame_with_detections = self.camera_handler.draw_detections(frame, response)
                
                report = self.report_generator.generate_report(response)
                print("\n" + "="*50)
                print(f"Security Report at {datetime.now().strftime('%H:%M:%S')}")
                print(report)
                
                cv2.imshow('Security Monitor', frame_with_detections)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user")
        finally:
            self.camera_handler.release_camera()
            cv2.destroyAllWindows()