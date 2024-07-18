import requests  
import json
def emotion_detector(text_to_analyze):
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputObj =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url,json=inputObj, headers =header )
    formatted_res = json.loads(response.text)
    max = 0
    dominant_emotion = None
    final_response = {}

    if(response.status_code==400):
        final_response['anger'] = None
        final_response['disgust'] = None
        final_response['fear'] = None
        final_response['joy'] = None
        final_response['sadness'] = None
    else:
        emotions =  formatted_res["emotionPredictions"][0]["emotion"]
        for emotion in emotions.keys():
            final_response[emotion]= emotions[emotion]
            if(emotions[emotion] > max):
                max = emotions[emotion]
                dominant_emotion = emotion  
    final_response["dominant_emotion"] = dominant_emotion
    return final_response
            
