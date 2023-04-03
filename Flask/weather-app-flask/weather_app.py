import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "5ba611a82ef84d1fa28160558230304"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        response = requests.get(BASE_URL, params={"key": API_KEY, "q": city})

        if response.ok:
            data = response.json()
            weather = {
                "city": data["location"]["name"],
                "country": data["location"]["country"],
                "temp": data["current"]["temp_c"],
                "description": data["current"]["condition"]["text"],
                "icon": data["current"]["condition"]["icon"],
            }
        else:
            weather = None

        return render_template("index.html", weather=weather)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
