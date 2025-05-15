import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=header)
    if response.status_code == 400:
        obj = {}
        for item in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']:
            obj[item] = None
        return obj

    formatted_response = json.loads(response.text)
    
    emotions_with_score = formatted_response['emotionPredictions'][0]['emotion']
    emotion_list = list(emotions_with_score.keys())
    emotion_scores = list(emotions_with_score.values())
    dominant_emotion_score = max(emotion_scores)
    index_of_dominant_emotion = emotion_scores.index(dominant_emotion_score)
    dominant_emotion = emotion_list[index_of_dominant_emotion]
    emotions_with_score['dominant_emotion'] = dominant_emotion

    return emotions_with_score 