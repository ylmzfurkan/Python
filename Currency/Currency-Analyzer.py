import requests
import pandas as pd


def get_exchange_rates(base_currency):
    url = f"https://api.exchangeratesapi.io/latest?base={base_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"API isteği başarısız: {response.status_code} - {response.text}")

    data = response.json()
    if "rates" not in data:
        raise Exception(f"Beklenen 'rates' anahtarı JSON verisinde bulunamadı: {data}")

    return data["rates"]


def main():
    base_currency = "USD"
    exchange_rates = get_exchange_rates(base_currency)

    # Döviz kurlarını bir DataFrame'e dönüştürün
    df = pd.DataFrame(list(exchange_rates.items()), columns=["Currency", "Rate"])

    # Döviz kurlarını büyükten küçüğe sıralayın
    df = df.sort_values(by="Rate", ascending=False)

    # Döviz kurlarını bir CSV dosyasına yazın
    df.to_csv("exchange_rates.csv", index=False)

    print("Döviz kurları başarıyla CSV dosyasına yazıldı.")

if __name__ == "__main__":
    main()
