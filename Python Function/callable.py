# callable() fonksiyonu, bir nesnenin çağrılabilir (callable) olup olmadığını kontrol eder ve 
# bu nesne çağrılabilir ise True, değilse False döndürür. Örneğin, bir fonksiyon veya sınıf 
# çağrılabilir bir nesnedir ancak bir sayı veya string çağrılabilir değildir.

# Örnek:

def greet(name):
    print("Hello, " + name)

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

# callable örneği
print(callable(greet))  # True
p = Person("Alice")
print(callable(p.greet))  # True

# callable olmayan örneği
print(callable("hello"))  # False
