# breakpoint() fonksiyonu, Python 3.7'de tanıtılmış bir hata ayıklama aracıdır ve programın 
# herhangi bir yerinde hata ayıklamak için kullanılır. Fonksiyon çağrıldığında program 
# çalışmayı durdurur ve ilgili satıra bir kesme noktası ekler. 

# Örnek olarak:

def multiply(a, b):
    result = a * b
    breakpoint()  # programı bu noktada durdurur
    return result

multiply(2, 5)


# Bu örnekte, breakpoint() fonksiyonu multiply() fonksiyonunun içinde çağrılır ve programın 
# çalışmasını durdurur. Bu noktada, hata ayıklayıcı açılır ve programın çalışması adım adım takip edilebilir.