from datetime import datetime
import anthropic
from dotenv import load_dotenv
import os

class ReportGenerator:
    def __init__(self):
        """Initialize Claude client for report generation."""
        load_dotenv()
        self.api_key = os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found")
        self.claude_client = anthropic.Anthropic(api_key=self.api_key)

    def generate_report(self, response):
        """Generate a natural language report using Claude."""
        # Prepare detection summaries
        objects = [f"{obj.name} (confidence: {obj.score:.2f})" 
                  for obj in response.localized_object_annotations]
        face_count = len(response.face_annotations)
        labels = [f"{label.description} (confidence: {label.score:.2f})" 
                 for label in response.label_annotations]

        # Create context for Claude
        context = f"""
        Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        Detections:
        - Objects detected: {', '.join(objects)}
        - Number of faces detected: {face_count}
        - Scene labels: {', '.join(labels)}
        """

        # Get Claude's analysis
        response = self.claude_client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=300,
            system="You are a security camera assistant. Analyze the detection results and provide a clear, concise security report. Focus on important security-relevant information.",
            messages=[{"role": "user", "content": f"Please analyze these security camera detections and provide a brief security report:\n{context}"}]
        )

        return response.content[0].text