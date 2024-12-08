# Security Vision Agent

A Python-based security camera system that uses Google Cloud Vision API for object/face detection and Claude AI for intelligent reporting. The system provides real-time monitoring with visual feedback and natural language analysis of the scene.

## Features

- Real-time video capture and processing
- Object and face detection using Google Cloud Vision API
- Intelligent scene analysis and reporting using Claude AI
- Visual annotations of detected objects and faces
- Timestamp overlay on video feed
- High-quality video capture (1280x720)

## Components

1. **CameraHandler**
   - Manages webcam capture
   - Handles visual annotations
   - Controls video quality

2. **VisionAnalyzer**
   - Processes frames through Google Cloud Vision
   - Detects objects and faces
   - Provides confidence scores

3. **ReportGenerator**
   - Generates natural language reports
   - Analyzes scene content
   - Provides security insights

4. **SecurityAgent**
   - Coordinates all components
   - Manages monitoring loop
   - Handles resource cleanup

## Flow of Operations
```
[Camera] → [Vision API] → [Claude AI] → [Display/Report]
   ↑           ↑             ↑              ↑
   └───────────┴─────────────┴──────────────┘
            SecurityAgent coordinates
```
```
1. Start Application
   └── Initialize SecurityAgent
       ├── Create CameraHandler
       ├── Create VisionAnalyzer
       └── Create ReportGenerator

2. Monitoring Loop
   ├── CameraHandler captures frame
   ├── VisionAnalyzer processes frame
   │   └── Sends to Google Cloud Vision
   ├── CameraHandler draws detections
   ├── ReportGenerator creates report
   │   └── Uses Claude for analysis
   └── Display results and report

3. Cleanup on Exit
   └── Release camera resources
```

## Prerequisites

Before running the agent, you need:

1. Python 3.7 or higher
2. Google Cloud account with Vision API enabled
3. Anthropic API key for Claude
4. Webcam or connected camera

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd vision_agent
```

2. Create and activate virtual environment:
```bash
# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
.\venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up credentials:
- Create a `.env` file and add your Anthropic API key:
  ```
  ANTHROPIC_API_KEY=your_key_here
  ```
- Set up Google Cloud credentials:
  ```bash
  export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
  ```

## Project Structure

```
vision_agent/
├── __init__.py
├── camera_handler.py      # Camera operations
├── vision_analyzer.py     # Google Cloud Vision integration
├── report_generator.py    # Claude AI reporting
├── security_agent.py      # Main orchestrator
└── main.py               # Entry point
```

## Usage

Run the security agent:
```bash
python main.py
```

Controls:
- Press 'q' to quit the application
- Press 'Ctrl+C' in terminal to stop

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Acknowledgments

- Google Cloud Vision API for object detection
- Anthropic's Claude for AI analysis
- OpenCV for camera handling
- Python community for various libraries

## Author

Luca Criscuolo

## Support

For support, please open an issue in the GitHub repository.