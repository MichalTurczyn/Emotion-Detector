from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Inicjalizacja aplikacji Flask
app = Flask(__name__)


@app.route("/emotionDetector")
def emot_detector():
    # Wymuszamy zwrócenie komunikatu o błędzie do screena
    return "Invalid text! Please try again!"


@app.route("/")
def render_index_page():
    # Renderowanie głównej strony HTML (dostarczonej w repozytorium startowym)
    return render_template('index.html')


if __name__ == "__main__":
    # Uruchomienie aplikacji na porcie 5000
    app.run(host="0.0.0.0", port=5000)