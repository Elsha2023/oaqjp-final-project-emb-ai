from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector
app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    data = request.get_json()
    text_to_analyze = data.get('text', '')
    result = emotion_detector(text_to_analyze)
    if 'error' in result:
        return jsonify({"error": result['error']}), 500
    # Format the response string as requested
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify({"response": response_text})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)