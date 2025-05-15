import requests, json, pprint

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text) # print(formatted_response) to see it
    
    emotions_with_score = formatted_response['emotionPredictions'][0]['emotion']
    emotion_list = list(emotions_with_score.keys())
    emotion_scores = list(emotions_with_score.values())
    dominant_emotion_score = max(emotion_scores)
    index_of_dominant_emotion = emotion_scores.index(dominant_emotion_score)
    dominant_emotion = emotion_list[index_of_dominant_emotion]

    emotions_with_score['dominant_emotion'] = dominant_emotion
    formatted_emotions_string = pprint.pformat(emotions_with_score, sort_dicts=False, indent=4)
    formatted_emotions_string = formatted_emotions_string.replace('{', '{\n').replace('}', '\n}')
    return formatted_emotions_string
    # return emotions_with_score