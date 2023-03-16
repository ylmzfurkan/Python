# aiter() fonksiyonu, bir iterable (yinelenebilir) nesnenin bir iterator (yinelenebilir) nesnesini döndürür. 
# Iterable nesneler, öğeleri üzerinde yinelemeye (iterasyon) izin veren nesnelerdir. aiter() fonksiyonu, 
# iterable bir nesne alır ve onun üzerinde yinelenebilir bir nesne döndürür.


# Burada, obj bir iterable nesnedir ve üzerinde yinelenebilir bir nesne döndürmek için kullanılır.

# Örnek olarak, bir liste üzerinde yineleyen bir iterator nesnesi oluşturabiliriz. Aşağıdaki örnekte, 
# önce bir liste oluşturuyoruz ve daha sonra aiter() fonksiyonunu kullanarak bu listeye bir iterator 
# nesnesi oluşturuyoruz. Daha sonra next() fonksiyonunu kullanarak, öğeleri teker teker okuyoruz:

# Bir liste oluşturalım
my_list = [1, 2, 3, 4, 5]

# Bir iterator nesnesi oluşturalım
my_iterator = iter(my_list)

# Öğeleri teker teker okuyalım
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3
print(next(my_iterator))  # 4
print(next(my_iterator))  # 5

# Bu örnekte, iter() fonksiyonu iterable nesne olan my_list nesnesini iterator nesnesi olan my_iterator 
# nesnesine dönüştürür. Daha sonra, next() fonksiyonunu kullanarak, my_iterator nesnesinin öğelerine erişiriz.