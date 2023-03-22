# Python'da classmethod() fonksiyonu, bir sınıfın örneği olmadan sınıfın metotlarının çağrılabilmesini sağlar. 
# Bu metot, sınıfın kendisini ilk argüman olarak alır (genellikle "cls" olarak adlandırılır) ve bu metodu 
# çağıran sınıfın referansını temsil eder.

# classmethod() fonksiyonu, özellikle sınıf yöntemleri (class methods) olarak adlandırılan metotları 
# tanımlamak için kullanılır. Sınıf yöntemleri, bir sınıfın örnekleriyle değil, doğrudan sınıf adı 
# üzerinden çağrılabilirler. Bu nedenle, sınıf yöntemleri genellikle sınıfın işlevselliğiyle ilgili 
# olan metotlar için kullanılır.

# Aşağıda, classmethod() fonksiyonunu kullanarak sınıf yöntemi tanımlama örneği verilmiştir:

# class MyClass:
#     count = 0
    
#     @classmethod
#     def increase_count(cls):
#         cls.count += 1
    
#     def __init__(self):
#         MyClass.increase_count()

# print(MyClass.count) # 0

# a = MyClass()
# b = MyClass()
# c = MyClass()

# print(MyClass.count) # 3

# Yukarıdaki örnekte, increase_count() metodu bir sınıf yöntemidir ve sınıfın referansını temsil eden "cls" 
# parametresini kullanarak sınıfın özelliklerini değiştirir. Bu metot, sınıfın örnekleriyle değil, doğrudan 
# sınıf adı üzerinden çağrılır.

# __init__() metodu, sınıfın her bir örneği oluşturulduğunda increase_count() metodunu çağırarak count 
# özelliğinin değerini artırır. Son olarak, MyClass.count özelliği, sınıfın örnekleri oluşturulduktan 
# sonra 3'e eşit olur.