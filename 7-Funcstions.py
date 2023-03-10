#Functions

# Python'da bir fonksiyon, belirli bir işlemi gerçekleştirmek için kullanılan ve 
# bir ad veya isim ile çağrılabilen bir bloktur. Bu işlem, programlama dilinde belirli 
# bir isim altında bir araya getirilerek, kodun tekrar tekrar yazılması önlenir ve daha 
# kolay yönetilir hale getirilir.

# Python'da bir fonksiyonu tanımlamak için "def" anahtar kelimesi kullanılır. Fonksiyon, 
# bir veya daha fazla parametre alabilir ve belirli bir kod bloğu içindeki işlemleri 
# gerçekleştirir. Fonksiyonun sonucu, "return" anahtar kelimesi ile belirtilir.

def toplama(a, b):
    c = a + b
    return c

x = toplama(2, 3)
print(x)

# Python programlama dilinde çok önemli bir kavramdır. Fonksiyonlar, tekrar 
# kullanılabilir kod bloklarıdır ve programlamada modülerliği sağlamak için kullanılırlar.

def kare_al(sayi):
    
# Verilen sayının karesini hesaplar.

# Args:
# sayi (int): Kare alınacak sayı.

# Returns:
# int: Kare değerini döndürür.
    
    kare = sayi ** 2
    return kare

# Fonksiyonu çağıralım
sonuc = kare_al(5)
print(sonuc)
