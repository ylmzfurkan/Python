# Python'da compile() fonksiyonu, verilen Python kodunu belirtilen bir dosya, 
# modül veya string olarak derler. Bu fonksiyon, derleme zamanında hataların 
# tespit edilmesini sağlar ve aynı kodu daha hızlı çalıştırmak için derleme 
# sonuçlarını önbelleğe alabilir.

# compile() fonksiyonunun kullanımı aşağıdaki gibidir:

# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

# source: derlenecek Python kodu, string veya AST (abstract syntax tree) nesnesi olarak verilir.
# filename: kodun kaynak dosyasının adı veya "stdin" olarak belirtilir.
# mode: kodun hangi modda derleneceği belirtilir. "exec", "eval" veya "single" modlarından biri olabilir.
# flags: derleme seçeneklerini belirlemek için kullanılır. Varsayılan olarak 0'dır.
# dont_inherit: True olarak ayarlanırsa, derleme seçenekleri üst sınıf ve alt modüllerden miras alınmaz. Varsayılan olarak False'dur.
# optimize: kodun ne kadar optimize edileceğini belirler. -1 (varsayılan) olarak ayarlandığında, optimizasyon yapılmaz.
# Aşağıda, compile() fonksiyonunun kullanımına örnek verilmiştir:

# code_str = 'a = 2\nb = 3\nprint(a + b)'
# code = compile(code_str, '<string>', 'exec')
# exec(code)

# Bu örnekte, compile() fonksiyonu, "code_str" değişkenindeki Python kodunu derler ve "code" adlı bir kod nesnesi döndürür. Bu nesne, exec() fonksiyonu tarafından çalıştırılır ve "a + b" ifadesinin sonucu olan 5 değeri ekrana yazdırılır.

# filename parametresi, derlenen kodun kaynak dosyasının adını belirlemek için kullanılır. Bu örnekte, <string> adı verilen bir sanal dosya kullanılmıştır. Bu, kodun bir dosyadan değil, bir string'den derlendiğini belirtir.

# mode parametresi, derlenen kodun hangi modda derleneceğini belirler. Bu örnekte, "exec" modu kullanılmıştır, yani kod bir modül ya da ifade değil, bir dizi ifade ve deyimler içerir.