# Python'da any() fonksiyonu, bir iterable'da en az bir True değeri 
# olduğunda True döndürür ve aksi takdirde False döndürür.

# Örneğin:

numbers = [1, 0, 3, 7, 0, 2]
result = any(numbers)

print(result)

# Bu kod, numbers listesinde en az bir tane doğru olan değer (1, 3, 7, 2) olduğu için True döndürür.