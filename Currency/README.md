# Currency Analyzer

Currency Analyzer, belirli bir temel para birimi (örneğin, "USD") için güncel döviz kurlarını alarak, bu verileri işler ve sonuçları bir CSV dosyasına yazar.

## Bağımlılıklar

Bu proje aşağıdaki Python kütüphanelerine bağımlıdır:

- `requests`
- `pandas`

Bağımlılıkları yüklemek için şu komutu kullanın:

pip install requests pandas


## Kullanım

Currency Analyzer'ı kullanmak için öncelikle, https://exchangeratesapi.io/ adresine giderek bir API anahtarı almanız gerekmektedir. Ardından, aşağıdaki kod satırını değiştirerek API anahtarınızı girin:

```python
access_key = "YOUR_ACCESS_KEY"  # Buraya gerçek API anahtarınızı ekleyin

Currency Analyzer'ı çalıştırmak için terminalde şu komutu kullanın:

python Currency-Analyzer.py

urrency Analyzer, temel para birimi için güncel döviz kurlarını alır ve "exchange_rates.csv" adlı bir CSV dosyasına yazar.

Özellikler
Temel para birimi için güncel döviz kurlarını alır.
Döviz kurlarını büyükten küçüğe sıralar.
Sıralanmış döviz kurlarını bir CSV dosyasına yazar.
Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için LICENSE dosyasına bakın.
