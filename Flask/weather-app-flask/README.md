# Hava Durumu Tahmin Uygulaması

Bu proje, kullanıcıların şehir adı girerek o şehir için mevcut hava durumu bilgilerini alabileceği basit bir Flask uygulamasıdır. WeatherAPI kullanılarak hava durumu verileri elde edilir.

## Kurulum

1. Bu projeyi yerel makinenize klonlayın veya indirin.

git clone https://github.com/ylmzfurkan/weather_app.git


2. Proje dizinine gidin ve sanal bir ortam oluşturun (isteğe bağlı):

cd weather_app
python3 -m venv venv


3. Sanal ortamı etkinleştirin:

- Windows:

venv\Scripts\activate


- Linux/MacOS:

source venv/bin/activate


4. Gerekli Python paketlerini yükleyin:

pip install -r requirements.txt


_Not: Bu proje için şu an sadece Flask paketi gerekmektedir._

5. `weather_app.py` dosyasında, `API_KEY` değişkenini WeatherAPI'den aldığınız API anahtarınızla değiştirin.

## Kullanım

1. Uygulamayı başlatın:

python weather_app.py


2. Tarayıcınızda `http://127.0.0.1:5000/` adresine gidin.

3. Şehir adını girin ve "Tahmin Et" düğmesine tıklayarak hava durumu bilgilerini görüntüleyin.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.
