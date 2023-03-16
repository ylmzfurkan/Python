# anext() fonksiyonu, bir iterator için bir sonraki öğeyi getirmek için kullanılan 
# bir Python fonksiyonudur. Eğer iterator'da bir sonraki öğe yoksa, StopIteration hatası verir. 

# Örneğin:

numbers = iter([1, 2, 3])

print(next(numbers))  # 1
print(next(numbers))  # 2
print(next(numbers)) # 3
print(anext(numbers)) # StopIteration hatası verir

# Bu örnekte, iter() fonksiyonu ile bir liste yarattık ve next() fonksiyonu ile sırayla ilk iki öğeyi 
# çağırdık. Sonrasında anext() fonksiyonu ile iterator'daki sonraki öğeyi çağırdık ve StopIteration hatası 
# almadık. Ancak, anext() fonksiyonunu tekrar çağırdığımızda StopIteration hatası verdi, çünkü listede başka bir öğe kalmamıştı.