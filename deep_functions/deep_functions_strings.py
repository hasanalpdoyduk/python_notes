#upper() fonksiyonu stringin tüm karakterlerini büyük harfe çevirir
#lower() fonksiyonu stringin tüm karakterlerini küçük harfe çevirir

#replace(x,y) fonksiyonu stringteki x değerlerini y ile değiştirir
print("Anne baba".replace("a","o"))
>>> Onne bobo
print("Kunduz".replace("duz","zun"))
>>> Kunzun
print("Python Programlama Dili".replace(" ","-"))
>>> Python-Programlama-Dili

#startswith(x) fonksiyonu string x ile başlıyorsa True, başlamıyorsa False değeri döndürür
#endswith(x) fonksiyonu string x ile bitiyorsa True, bitmiyorsa False değeri döndürür
print("Python".startswith("Py"))
>>> True
print("Python".endswith("az"))
>>> False

#split(a) fonksiyonu verilen bir a değerine göre string parçalara ayrılarak herbir parça listeye atılır
liste = "Python Programlama Dili".split(" ") #boşluk karakterine göre ayrıldı
print(liste)
>>> ['Python', 'Programlama', 'Dili']

#strip(x) fonksiyonu stringin başında ve sonunda bulunan x değerlerini siler
#lstrip(x) fonksiyonu stringin sadece başında bulunan x değerlerini siler
#rstrip(x) fonksiyonu stringin sadece sonunda bulunan x değerlerini siler
print("                   python                          ".strip()) #değer göndermezsek varsayılan olarak boşluk karakteri
>>> python
print(">>>>>>>>>>>>>>Mustafa>>>>>>>>>>>>>>>>>>>>>>>>>>".lstrip(">"))
>>> Mustafa>>>>>>>>>>>>>>>>>>>>>>>>>>

#join() fonksiyonu listenin elemanlarını bir string değeriyle birleştirmeyi sağlar
liste = ["21","02","2014"]
print("/".join(liste))
>>> 21/02/2014

#count(x,index) fonksiyonu stringin içindeki x değerlerini verilen index değerinden başlayarak saymaya başlar
print("ada kapısı yandan çarklı".count("a"))
>>> 6
print("ada kapısı yandan çarklı".count("a",2))
>>> 5

#find(x) fonksiyonu x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir
#rfind(x) fonksiyonu x değerini sondan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir
print("araba".find("a"))
>>> 0
print("araba".find("s"))
>>> -1
print("araba".rfind("a"))
>>> 4
