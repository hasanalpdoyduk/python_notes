#set bir elemandan sadece bir adet tutan bir veri tipidir
liste = [1,2,3,3,1,1,2,2,2]
x = set(liste)
print(x) #aynı elemanlar tek bir elemana indirgendi
>>> {1, 2, 3}

x = {"Python","Php","Python"}
print(x) #aynı elemanlar teke indirgendi
>>> {'Php', 'Python'}

#set'ler de tıpkı sözlükler gibi sırasız bir veri tipidir
x = {"Python","Php","Java","C","Javascript"}
for i in x:
    print(i) 
>>> Php
		Python
		Java
		Javascript
		C
#set'lerin bir elemanına direkt index ile ulaşamayız
#set'leri listeye çevirip index işlemlerini uygulayabiliriz

#add() fonksiyonu
x = {1,2,3}
x.add(4)
print(x)
>>> {1, 2, 3, 4}
x.add(4) #tekrar eklenmiyor
print(x)
>>> {1, 2, 3, 4}

#difference() fonksiyonu
küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
print(küme1.difference(küme2))
>>> {-2, 3, 10, 100}
print(küme2.difference(küme1))
>>>{-1, 23}
#difference_update() fonksiyonu ile difference() fonksiyonunda ulaşılan sonuç set'e yazılır

#discard() fonksiyonu
küme1 = {1,2,3,4,5,6}
küme1.discard(2)
print(küme1)
>>> {1, 3, 4, 5, 6}
küme1.discard(10) #olmayan değeri çıkarmıyor
print(küme1)
>>> {1, 3, 4, 5, 6}

#intersection() fonksiyonu
küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
print(küme1.intersection(küme2))
>>> {1, 2, 34}
#intersection_update() fonksiyonu ile intersection() fonksiyonunda ulaşılan sonuç set'e yazılır

#isdisjoint() fonksiyonu ayrık küme olup olmadıklarını denetler
küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme3 = {30,40,50}
print(küme1.isdisjoint(küme2))
>>> False
print(küme1.isdisjoint(küme3))
>>> True

#issubset() fonksiyonu alt küme olup olmadıklarını denetler
küme1 = {1,2,3}
küme2 = {1,2,3,4}
küme3 = {5,6,7}
print(küme1.issubset(küme2))
>>> True
print(küme1.issubset(küme3))
>>> False

#union() fonksiyonu iki kümenin birleşim kümesini oluşturur
küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
print(küme1.union(küme2))
>>> {-2, -1, 1, 2, 3, 10, 23, 34, 100}

#update() fonksiyonu iki kümenin birleşim kümesini oluşturur, uygulanan set'e yazılır
