# Python'da complex() fonksiyonu, gerçek ve sanal sayılarla birlikte karmaşık sayılar 
# oluşturmak için kullanılır. Bu fonksiyon, bir veya iki argüman alabilir. Eğer bir 
# argüman verilirse, argümanın karmaşık kısmı 0 olarak kabul edilir.

# complex() fonksiyonunun kullanımı aşağıdaki gibidir:

# complex([real[, imag]])

# real: karmaşık sayının gerçek kısmıdır. Varsayılan olarak 0'dır.
# imag: karmaşık sayının sanal kısmıdır. Varsayılan olarak 0.0'dır.
# Aşağıda, complex() fonksiyonunun kullanımına örnek verilmiştir:

# a = complex(2, 3)
# b = complex(4)
# c = complex()

# print(a) # (2+3j)
# print(b) # (4+0j)
# print(c) # 0j

# Bu örnekte, complex() fonksiyonu, a değişkenine 2 + 3j, b değişkenine 4 + 0j (veya sadece 4) ve c değişkenine 0j (yani sadece 0) değerlerini atar.

# İlk argüman gerçek kısımı, ikinci argüman ise sanal kısmı belirtir. Bu örnekte, a değişkenine 2 + 3j 
# değeri atanırken, gerçek kısım 2, sanal kısım ise 3'tür. b değişkeni ise, yalnızca bir argüman aldığı 
# için gerçek kısmı 4 ve sanal kısmı 0 olacak şekilde atanmıştır. c değişkeni ise hiçbir argüman almadığı için 0j değerini almıştır.