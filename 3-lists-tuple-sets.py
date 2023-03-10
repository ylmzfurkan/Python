#Lists-Tuple-Sets

# .append(item): Listenin sonuna bir öğe ekler.
# .extend(iterable): Listenin sonuna, bir iterable'ın tüm öğelerini ekler.
# .insert(index, item): Belirtilen konuma bir öğe ekler.
# .remove(item): İlk olarak belirtilen öğeyi listeden kaldırır.
# .pop([index]): Listenin belirtilen konumundan bir öğeyi kaldırır ve değerini döndürür. Eğer index belirtilmezse son öğe kaldırılır.
# .index(item): Belirtilen öğenin indeksini döndürür.
# .count(item): Belirtilen öğenin listenin içinde kaç kez tekrarlandığını sayar.
# .sort(): Listenin öğelerini sıralar.
# .reverse(): Listenin öğelerini ters çevirir.
# .copy(): Listenin bir kopyasını döndürür.

# courses = ["History" , "Math" , "Physics" , "CompSci"]
# courses_2 = ["Art" , "Education"]
# courses.append("Art")
# courses.insert(0 , "Art")
# courses.extend(courses_2)
# courses.remove("Math")
# print(courses)
# print(courses[0])
# print(courses[-1])
# print(courses[0:2])

# nums = [2, 4, 7, 1, 9, 3]
# nums.sort()
# nums.reverse()
# print(nums)
# for index, course in enumerate(courses, start = 1):
#     print(index, course)

# Listeler: Python'da, birden fazla öğeyi depolamak için kullanabileceğiniz bir veri yapısıdır. 
# Listeler, köşeli parantez içine alınmış öğelerden oluşur ve öğeler arasında virgülle ayrılır. 
# Örneğin:

# my_list = ["elma", "armut", "çilek"]

# Tuple: Tuple'lar, listelere benzer, ancak değiştirilemezdir. 
# Yani, bir tuple bir kez oluşturulduktan sonra, öğeleri değiştirilemez veya silinemez. 
# Tuple'lar da virgülle ayrılmış öğelerden oluşur ve öğeler parantez içinde yer alır. 
# Örneğin:

# my_tuple = ("elma", "armut", "çilek")

# Setler: Set'ler, benzersiz öğeleri depolamak için kullanılır ve öğelerin sırası önemli değildir. 
# Set'ler, süslü parantez içine alınmış öğelerden oluşur ve öğeler arasında virgülle ayrılır. 
# Örneğin:

# my_set = {"elma", "armut", "çilek"}

# Listeler: değiştirilebilir ve sıralıdır. 
# Aynı öğeyi birden fazla kez içerebilir ve indeksleme veya dilimleme gibi birçok işlevselliğe sahiptir.

# Tuple: değiştirilemez ve sıralıdır. Listelerden daha hızlıdır ve bir kez 
# oluşturulduktan sonra, öğeleri değiştirilemez veya silinemez.

# Setler: değiştirilebilir ve sırasızdır. Her öğe yalnızca bir kez yer alabilir ve matematiksel set işlemlerini 
# gerçekleştirme özelliklerine sahiptir (birleştirme, kesişim, vb.).

# set1 = {1, 2, 3, 4, 5} #Set
# set2 = {3, 4, 5, 6, 7} #Set
# intersection_set = set1.intersection(set2) #Ortak elemanları bulur.
# print(intersection_set)  # {3, 4, 5}

# intersection, iki veya daha fazla kümenin ortak elemanlarını bulmak için kullanılan bir kümeler arası işlemdir. 
# Bu işlem sonucunda, ortak olan elemanlar yeni bir küme olarak döndürülür.

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# difference_set = set1.difference(set2) #Farklı elemanları bulur.
# print(difference_set)  # {1, 2}

# difference(), iki veya daha fazla küme arasındaki farklı elemanları bulmak için kullanılan bir kümeler arası işlemdir. 
# Bu işlem sonucunda, ilk kümede bulunan, ancak diğer kümede bulunmayan elemanlar yeni bir küme olarak döndürülür.

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# union_set = set1.union(set2) #Kümelerin birleşimini bulur, ortakları 1 kere yazar.
# print(union_set)  # {1, 2, 3, 4, 5, 6, 7}

# union(), iki veya daha fazla kümenin birleşimini bulmak için kullanılan bir kümeler arası işlemdir. 
# Bu işlem sonucunda, her iki veya daha fazla kümenin tüm elemanları yeni bir küme olarak döndürülür.