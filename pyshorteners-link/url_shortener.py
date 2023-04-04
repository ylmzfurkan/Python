import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

if __name__ == "__main__":
    long_url = input("Uzun URL'yi girin: ")
    short_url = shorten_url(long_url)
    print(f"Kısaltılmış URL: {short_url}")
