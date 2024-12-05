from camera_handler import CameraHandler
from vision_analyzer import VisionAnalyzer
from report_generator import ReportGenerator
from security_agent import SecurityAgent

def main():
    try:
        # Initialize components
        camera_handler = CameraHandler()
        vision_analyzer = VisionAnalyzer()
        report_generator = ReportGenerator()
        
        # Create and start security agent
        agent = SecurityAgent(camera_handler, vision_analyzer, report_generator)
        agent.monitor()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()