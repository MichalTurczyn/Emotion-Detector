from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Inicjalizacja aplikacji Flask
app = Flask(__name__)


@app.route("/emotionDetector")
def emot_detector():
    # Pobranie tekstu przesłanego w adresie URL (argument 'textToAnalyze')
    text_to_analyze = request.args.get('textToAnalyze')

    # Wywołanie funkcji analizującej emocje
    response = emotion_detector(text_to_analyze)

    # Wyciągnięcie wartości z otrzymanego słownika
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Zadanie 7: Obsługa błędu dla pustego lub nieprawidłowego wejścia
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Zwrócenie sformatowanej odpowiedzi tekstowej dla interfejsu użytkownika
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    # Renderowanie głównej strony HTML (dostarczonej w repozytorium startowym)
    return render_template('index.html')


if __name__ == "__main__":
    # Uruchomienie aplikacji na porcie 5000
    app.run(host="0.0.0.0", port=5000)