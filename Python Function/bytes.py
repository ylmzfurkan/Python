# bytes() fonksiyonu, belirtilen değerleri (örneğin, bir dize) byte dizisi olarak döndürür ve değiştirilemeyen bir veri tipidir. 

#Bir örnek olarak:

# String değerini bytes dizisine dönüştürme
string_degeri = "Merhaba Dünya"
bytes_dizisi = bytes(string_degeri, encoding='utf-8')

print(bytes_dizisi)  # b'Merhaba D\xc3\xbcnya'

# Bu örnekte, "Merhaba Dünya" adlı dize, bytes() fonksiyonu kullanılarak UTF-8 kodlaması kullanılarak byte dizisine dönüştürülür. b ön ek, değerin byte dizisi olduğunu belirtir.



