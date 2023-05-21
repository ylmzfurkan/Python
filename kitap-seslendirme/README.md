# Text-to-Speech Kitap Seslendirme Uygulaması

Bu proje, bir metni otomatik olarak sesli bir formatta okuyan bir Python uygulamasıdır. Uygulama Google'ın Text-to-Speech (gTTS) API'sini kullanır.

## Kurulum

Uygulamanın çalışabilmesi için gereken bağımlılıklar aşağıdaki gibidir:

- Python 3.6 ve üzeri
- gTTS
- mpg123

Python'ı [resmi Python web sitesi](https://www.python.org/) üzerinden indirebilirsiniz. gTTS ve mpg123'ü ise pip kullanarak indirebilirsiniz:

pip install gTTS

mpg123'ü aşağıdaki bağlantıyı kullanarak indirebilirsiniz:
- [mpg123 Download](https://www.mpg123.de/download.shtml)

## Kullanım

Uygulamanın kullanımı oldukça basittir. Metni okumasını istediğiniz kitabın txt dosyasını 'kitap-seslendirme' klasörüne kopyalayın ve ismini 'kitap.txt' olarak değiştirin. Daha sonra uygulamayı çalıştırın:

python3 metin_okuma.py


Uygulama, 'kitap.txt' dosyasındaki metni okuyacak ve 'speech.mp3' adlı bir ses dosyası oluşturacaktır.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.
