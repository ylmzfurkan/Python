# WhatsApp Otomatik Mesaj Gönderme

Bu proje, belirli zaman aralıklarında seçilen kişilere veya gruplara WhatsApp üzerinden otomatik olarak mesaj göndermeyi sağlar. Projede, Selenium WebDriver ile Python kullanılmıştır.

## Özellikler

- Belirli zaman aralıklarında otomatik mesaj gönderme
- Seçilen kişilere veya gruplara mesaj gönderme
- messages.txt dosyasından rastgele mesaj seçme

## Kurulum

1. Projeyi klonlayın veya indirin:

git clone https://github.com/ylmzfurkan/whatsapp-auto-message.git

2. Gerekli paketleri yükleyin:

pip install -r requirements.txt


3. Google Chrome WebDriver'ı indirin ve proje dizinine kopyalayın:
   https://sites.google.com/a/chromium.org/chromedriver/downloads

4. config.py dosyasında gerekli ayarları yapın (telefon numarası, mesaj gönderilecek kişi veya grup adı, mesaj gönderme zaman aralığı vb.)

5. Projeyi çalıştırın:

python message.py

## Kullanım

1. Proje çalıştırıldığında, QR kodu telefonunuzdan tarayarak WhatsApp Web'e bağlanın.
2. Ayarladığınız zaman aralığına göre, seçilen kişi veya gruplara otomatik olarak mesaj gönderilecektir.

## Lisans

Bu proje, MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.
