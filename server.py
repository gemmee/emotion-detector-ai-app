from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    if (text_to_analyze):
        response = emotion_detector(text_to_analyze)
    else:
        response = None

    if response:
        # Extract the scores of all the emotions and the dominant emotion
        anger_s = response['anger']
        disgust_s = response['disgust']
        fear_s = response['fear']
        joy_s = response['joy']
        sadness_s = response['sadness']
        dominant_emotion = response['dominant_emotion']
        
        return f"For the given statement, the system response is 'anger': {anger_s},\
        'disgust': {disgust_s}, 'fear': {fear_s}, 'joy': {joy_s}\
        and 'sadness': {sadness_s}. The dominant emotion is {dominant_emotion}."
    
    elif response is None:
        return "Invalid input! Try again."


@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
