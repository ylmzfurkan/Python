# Python'da all() fonksiyonu, verilen bir iterable'daki tüm elemanların True veya truthy 
# değer döndürmesi durumunda True, aksi takdirde False değerini döndürür.

# Örneğin, aşağıdaki kod bloğunda all() fonksiyonu kullanarak bir liste içerisindeki tüm 
# elemanların pozitif olduğunu kontrol edebiliriz:

numbers = [1, 2, 3, 4, 5]
result = all(num > 0 for num in numbers)
print(result) # True

# Yukarıdaki örnekte, all() fonksiyonu ile numbers listesindeki her bir elemanın 0'dan büyük 
# olduğunu kontrol ediyoruz. Sonuç olarak, tüm elemanlar pozitif olduğu için True değeri döndürülür.



