#extend() fonksiyonu listeye liste halinde eleman eklememizi sağlar
liste = [1,2,3,4,5,6,7]
liste.extend([10,11,12])
print(liste)
>>> [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]

#insert() fonksiyonu listenin belli bir indeksine bir eleman eklememizi sağlar
liste = [1,2,3,4,5,6,7,8,9]
liste.insert(2, "Python")
print(liste)
>>> [1, 2, 'Python', 3, 4, 5, 6, 7, 8, 9]

#pop() fonksiyonu içine hiçbir değer vermezsek listenin son elemanını siler ve ekrana basılabilir
#pop() fonksiyonu içine belli bir indeks değeri verirsek o indeksi siler ve ekrana basılabilir
liste = [1,2,3,4,5,6,7]
liste.pop() #son eleman siliniyor
print(liste)
>>> [1, 2, 3, 4, 5, 6]
print(liste.pop(2)) #2.indeksteki eleman siliniyor
>>> 3
print(liste)
>>> [1, 2, 4, 5, 6]

#remove() fonksiyonu verdiğimiz değeri listeden çıkarmamızı sağlar
liste = ["Python","Php","Java","C"]
liste.remove("Python") 
print(liste)
>>> ['Php', 'Java', 'C']

#index() fonksiyonu verilen bir değerin baştan başlayarak hangi indekste olduğunu söyler
liste = [1,2,3,4,3,3,5,6,7,8,9]
print(liste.index(3))
>>> 2
#eğer ekstra index değeri belirtilirse, index() fonksiyonu değeri bu indeksten itibaren aramaya çalışır
print(liste.index(3,3)) #3 elemanını 3.indekten itibaren arar
4

#count() fonksiyonu verilen bir değerin listede kaç defa geçtiğini sayar
liste = [1,2,3,4,5,6,1,1,1,1,1,1,1,1,8]
print(liste.count(1))
>>> 9

#sort() metodu bir listenin elemanlarını sayıysa küçükten büyüğe, string ise alfabetik olarak sıralar
liste = [12,-2,3,1,34,100]
liste.sort()
print(liste)
>>> [-2, 1, 3, 12, 34, 100]
liste2 = ["Python","Php","C","Java"]
liste2.sort()
print(liste2)
>>> ['C', 'Java', 'Php', 'Python']
#eğer özellikle içine reverse = True değeri verilirse elemanları büyükten küçüğe sıralar
liste = [12,-2,3,1,34,100]
liste.sort(reverse = True)
print(liste)
>>> [100, 34, 12, 3, 1, -2]
