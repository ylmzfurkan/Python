import requests
import time

def get_crypto_data(crypto):
    url = f'https://api.coinpaprika.com/v1/tickers/{crypto}'
    response = requests.get(url)
    data = response.json()
    return data

def display_crypto_data(crypto_data):
    print(f"{crypto_data['name']} ({crypto_data['symbol']})")
    print(f"Price: ${crypto_data['quotes']['USD']['price']}")
    print(f"24h Change: {crypto_data['quotes']['USD']['percent_change_24h']}%")
    print()

watchlist = [
    'btc-bitcoin',
    'eth-ethereum',
    'bnb-binance-coin',
    'ada-cardano',
    'xrp-xrp',
    'sol-solana',
    'dot-polkadot',
    'avax-avalanche', 
    'doge-dogecoin',
    'matic-polygon'
]


while True:
    for crypto in watchlist:
        try:
            crypto_data = get_crypto_data(crypto)
            display_crypto_data(crypto_data)
        except Exception as e:
            print(f"Error fetching data for {crypto}: {e}")
    time.sleep(60)  # 60 saniyede bir verileri güncelle
