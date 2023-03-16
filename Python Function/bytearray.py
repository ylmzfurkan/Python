# bytearray() fonksiyonu, belirtilen argümanlara sahip bir dizi oluşturarak ve bu dizideki 
# her öğe için 0 ile 255 arasında bir tam sayı olacak şekilde değiştirerek bir byte nesnesi 
# döndürür. Bu fonksiyon özellikle, bir değişkene atamadan önce verileri değiştirmeniz gereken durumlarda kullanışlıdır. 

# Örneğin:

# 16 bitlik bir veri dizisi oluşturma
data = bytearray([0x45, 0x32, 0x12, 0xff])
print(data)  # b'E2\x12\xff'


# Burada, bytearray() fonksiyonu 0x45, 0x32, 0x12 ve 0xff verilerini içeren bir byte nesnesi 
# oluşturuyor ve data değişkenine atıyor. print() fonksiyonu bu değişkeni yazdırıyor.



