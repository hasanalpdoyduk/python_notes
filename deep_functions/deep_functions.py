#lambda fonksiyonu ile fonksiyon yaratma
double = lambda x : x * 2
double(4)
>>> 8

#map() fonksiyonu gönderilen fonksiyonu her bir eleman üzerine uygular
def double(x):
    return x * 2
list(map(double, [1, 2, 3, 4, 5, 6, 7])
#sonuçları tutacak bir veri tipiyle birlikte kullanılmalıdır
list(map(lambda x : x ** 2, [1, 2, 3, 4, 5, 6, 7])) #lambda ile kullanılabilir

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
list(map(lambda x,y : x * y , liste1,liste2))
>>> [5, 12, 21, 32]

#reduce() fonksiyonu gönderilen fonksiyonu bir sağdaki elemana göndererek ilerler
from functools import reduce  #reduce fonksiyonu son sürümlerde functools modülüne taşındı
def toplama(x, y):
		return x + y
reduce(toplama, [12,18,20,10])
>>> 60
reduce(lambda x,y : x + y , [12,18,20,10]) #lambda ile kullanılabilir
>>> 60

#filter() fonksiyonu gönderilen mantıksal değer fonksiyonunu her bir elemana uygular
#sonuçları tutacak bir veri tipiyle birlikte kullanılmalıdır
print(list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9,10])))
>>> [2, 4, 6, 8, 10]

def asal_mi(x):
    i = 2
    if (x == 1):
        return False #asal değil
    elif(x == 2):
        return True #asal sayı
    else:
        while(i < x):
            if (x % i == 0):
                return False #asal Değil
            i += 1
    return True
print(list(filter(asal_mi,range(1,100)))) #1 den 100' e kadar olan asal sayılar
>>> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#zip() fonksiyonu liste elemanlarını gruplamakta (birleştirmekte) kullanılır
#sonuçları tutacak bir veri tipiyle birlikte kullanılmalıdır
liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]
print(list(zip(liste1,liste2)))
>>> [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
#aynı anda iki liste üzerinde gezinmek
liste1 = [1,2,3,4]
liste2 = ["Python","Php","Java","Javascript"]
for i,j in zip(liste1,liste2):
    print("i:",i,"j:",j)
>>> i: 1 j: Python
		i: 2 j: Php
		i: 3 j: Java
		i: 4 j: Javascript

#enumerate() fonksiyonu listedeki elemanın indexini ve elemanı gösterir
#sonuçları tutacak bir veri tipiyle birlikte kullanılmalıdır
liste = ["Elma","Armut","Muz","Kiraz"]
print(list(enumerate(liste)))
>>> [(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Kiraz')]

#all() fonksiyonu bütün değerler True ise True, en az bir değer False ise False sonuç döndürür
#any() fonksiyonu bütün değerler False ise False, en az bir değer True ise True sonuç döndürür
