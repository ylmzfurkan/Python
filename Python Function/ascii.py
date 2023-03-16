# ascii() fonksiyonu, bir nesnenin ASCII formatındaki temsilini döndürür.

# Örneğin:

print(ascii("şöçğüİı"))
"'\\u015f\\xf6\\xe7\\u011f\\xfc\\u0130\\u0131'"

# Bu örnekte, ascii() fonksiyonu, Türkçe karakterler içeren bir stringi ASCII 
# formatına çevirerek Unicode kaçış dizileri kullanarak temsil eder.