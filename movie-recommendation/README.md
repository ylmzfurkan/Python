# Film Öneri Sistemi

Film Öneri Sistemi, kullanıcıların belirli bir filme benzer filmleri bulmalarına yardımcı olan basit bir Python uygulamasıdır. Bu uygulama, filmler arasındaki benzerliği ölçmek için kozinüs benzerliği kullanır.

## Gereksinimler

- Python 3.6+
- pandas
- scikit-learn

## Kurulum

1. Bu projeyi yerel makinenize klonlayın:

git clone https://github.com/ylmzfurkan/film-oneri-sistemi.git


2. Gerekli Python paketlerini yükleyin:

pip install -r requirements.txt


## Kullanım

1. `movie.py` betiğini çalıştırın:

python movie.py


2. Belirli bir filmle ilgili öneriler almak için, betiğin içinde `movie_title` değişkenini aradığınız filmle güncelleyin ve betiği tekrar çalıştırın.

```python
movie_title = "The Dark Knight"

3. Önerilen filmler, betiğin çıktısı olarak görüntülenecektir.

Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.


Bu README.md dosyasını, projenizin ana dizininde oluşturun ve yukarıdaki içeriği dosyaya yapıştırın. README dosyasında kullanıcı adınızı ve projenizin GitHub URL'sini doğru bir şekilde güncellemeyi unutmayın.
