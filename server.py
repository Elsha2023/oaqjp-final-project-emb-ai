"""Flask application for emotion detection using Watson NLP service."""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_Detector():
    """
    Endpoint to process emotion detection for input text.

    Expects a JSON payload with key 'text'.
    Returns a JSON response with emotion scores and dominant emotion,
    or an error message if input is invalid.
    """
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    result = emotion_detector(text_to_analyze)

    if 'error' in result:
        return jsonify({"error": result['error']}), 500

    if result.get('dominant_emotion') is None:
        return jsonify({"response": "Invalid text! Please try again!"})

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response_text})

@app.route('/')
def index():
    """
    Render the index.html homepage.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
