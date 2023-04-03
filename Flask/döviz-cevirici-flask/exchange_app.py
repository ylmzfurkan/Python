import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "e0543d0834864ab4b66845b6eb1a4e6a"
BASE_URL = "https://openexchangerates.org/api/"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        base_currency = request.form["base_currency"]
        target_currency = request.form["target_currency"]
        date = request.form["date"]

        response = requests.get(f"{BASE_URL}historical/{date}.json", params={"app_id": API_KEY, "base": base_currency, "symbols": target_currency})
        print(response.url)  # URL'yi yazdırın
        print(response.text)  # Yanıt içeriğini yazdırın

        if response.ok:
            data = response.json()
            if "rates" in data and target_currency in data["rates"]:
                exchange_rate = data["rates"][target_currency]
            else:
                exchange_rate = None
                print("Hedef para birimi 'rates' anahtarında bulunamadı.")  # Hedef para birimi eksikse yazdırın
        else:
            exchange_rate = None
            print("API yanıtı başarısız oldu.")  # API yanıtı başarısızsa yazdırın

        return render_template("index.html", exchange_rate=exchange_rate, base_currency=base_currency, target_currency=target_currency)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
