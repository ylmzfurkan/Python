#İmport

# Python'da bir modül, farklı programlama dosyalarında kullanılabilecek kod kütüphaneleridir. 
# Modüller, başka bir dosyada yazılmış olan Python kodu kütüphanelerini içerirler ve kodun 
# yeniden kullanılabilirliğini artırırlar.

# Python'da bir modülü kullanmak için "import" anahtar kelimesini kullanabiliriz. 
# Örneğin, "math" modülünü kullanmak istiyorsak, şu şekilde kullanabiliriz:

import math

# Math modülündeki fonksiyonları keşfetmek için
print(dir(math))

# Bu kodda, "dir()" fonksiyonu kullanılarak "math" modülündeki fonksiyonlar ve 
# değişkenler listelendi. Bu sayede, modüldeki hangi fonksiyonların kullanılabileceğini öğrenebiliriz.

# Math modülündeki sqrt fonksiyonunu nasıl kullanacağımızı öğrenmek için
help(math.sqrt)
