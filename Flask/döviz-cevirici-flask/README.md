# Döviz Kuru Dönüşüm Uygulaması

Bu Flask uygulaması, belirli bir tarihte iki para birimi arasındaki döviz kuru dönüşüm oranını gösterir. Uygulama, Open Exchange Rates API'sini kullanarak döviz kuru bilgilerini alır.

## Kurulum

1. Bu depoyu klonlayın veya indirin:

git clone https://github.com/ylmzfurkan/your-repo.git
cd your-repo


2. Sanal bir ortam oluşturun ve etkinleştirin:

python3 -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows


3. Gerekli paketleri yükleyin:

pip install -r requirements.txt


4. Open Exchange Rates API anahtarınızı `exchange_app.py` dosyasındaki `API_KEY` değişkenine ekleyin:

```python
API_KEY = "YOUR_OPENEXCHANGERATES_API_KEY"

Kullanım
Uygulamayı başlatın:

python exchange_app.py
arayıcınızda http://127.0.0.1:5000/ adresini açın.

Tarih, temel para birimi ve hedef para birimini girin.

"Dönüşüm Oranı" butonuna tıklayarak iki para birimi arasındaki döviz kuru dönüşüm oranını görüntüleyin.

Lisans
Bu proje, MIT Lisansı ile lisanslanmıştır.
