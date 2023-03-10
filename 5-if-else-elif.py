#İf - Else - Elif
# Python'da if, else ve elif (else if'in kısaltması) ifadeleri, belirli koşullar altında farklı işlemler yapmak için kullanılır. 
# Bu ifadeler, programların mantıksal akışını yönetmek için oldukça önemlidir. 
# Kısaca if, else ve elif ifadelerini aşağıdaki şekilde özetleyebiliriz:

# if: Bir koşul sağlandığında belirli bir işlem yapmak için kullanılır. 
# Koşul doğru olduğunda, if bloğu içindeki işlemler çalıştırılır. Örneğin:

x = 10
if x > 0:
    print("x pozitif")

# else: if bloğundaki koşul yanlışsa yapılacak işlemleri tanımlamak için kullanılır. 
# Bir else bloğu, bir if bloğuyla eşleştirilmelidir. Örneğin:

x = -5
if x > 0:
    print("x pozitif")
else:
    print("x negatif veya sıfır")

# elif: Bir dizi koşul altında farklı işlemler yapmak için kullanılır. 
# elif blokları, bir if bloğu veya bir başka elif bloğuyla eşleştirilmelidir ve 
# son else bloğundan önce kullanılmalıdır. Örneğin:

x = 0
if x > 0:
    print("x pozitif")
elif x < 0:
    print("x negatif")
else:
    print("x sıfır")
