#Loop and İteration

# Python'da "loop" ve "iteration" kavramları, belirli bir 
# işlemi tekrarlamak için kullanılan programlama yapılarıdır.

# for loop: Belirli bir dizi üzerinde gezinmek için kullanılır. Bu döngü, 
# belirli bir dizi veya listedeki öğeleri birer birer alır ve belirli bir kod bloğu içinde işler. 
# Örneğin:

for i in range(5):
    print(i)


# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     if num == 3:
#         print("Var")
#         continue
#     print(num)

# for num in nums:
#     for letter in "abc":
#         print(num, letter)

# for i in range(1,11):
#     print(i)

# while loop: Belirli bir koşul sağlandığı sürece belirli bir kod bloğunu tekrar tekrar çalıştırmak için 
# kullanılır. while döngüsü, belirli bir koşul sağlandığı sürece döngü içindeki kod bloğunu tekrar tekrar çalıştırır. 
# Örneğin:

x = 0

while x < 15:
    print(x)
    x += 1
