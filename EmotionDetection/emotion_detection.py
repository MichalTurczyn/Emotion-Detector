import requests
import json


def emotion_detector(text_to_analyze):
    # Adres URL dla usługi Watson NLP Emotion Predict
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Nagłówki wymagane przez API Watson
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Dane wejściowe w formacie JSON
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Wysłanie zapytania POST do API
    response = requests.post(url, json=myobj, headers=headers)

    # Zadanie 7: Obsługa statusu kodu 400 (pusty lub błędny input)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parsowanie odpowiedzi JSON przy udanej operacji (Status 200)
    formatted_response = json.loads(response.text)

    # Wyciągnięcie punktacji dla poszczególnych emocji
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotion_predictions['anger']
    disgust_score = emotion_predictions['disgust']
    fear_score = emotion_predictions['fear']
    joy_score = emotion_predictions['joy']
    sadness_score = emotion_predictions['sadness']

    # Zadanie 3: Znalezienie emocji dominującej (o najwyższej wartości)
    emotions_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)

    # Zwrócenie sformatowanego słownika wyjściowego
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }