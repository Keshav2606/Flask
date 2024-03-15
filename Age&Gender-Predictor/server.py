from flask import Flask, render_template
import requests

app = Flask(__name__)

AGIFY_URL = "https://api.agify.io"
GENDERIZE_URL = "https://api.genderize.io"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/guess/<name>")
def guess(name):
    name_param = {
        "name": name,
    }

    agify_response = requests.get(AGIFY_URL, params=name_param)
    agify_response.raise_for_status()
    agify_data = agify_response.json()

    genderize_response = requests.get(GENDERIZE_URL, params=name_param)
    genderize_response.raise_for_status()
    genderize_data = genderize_response.json()
    return render_template("guess.html", name=name.title(), gender=genderize_data["gender"], age=agify_data["age"])


if __name__ == '__main__':
    app.run(debug=True)
