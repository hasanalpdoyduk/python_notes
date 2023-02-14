\n #satır atlama
\t #tab (4) boşluk

#sep parametresi 
#elemanlar arası boşluğu değiştirme
#python'da otomatik atanan tek boşluğu değiştime
print("10", "05", "2002", sep = "/")
>>> 10/05/2002

print("Hasan", "Alp", "Doyduk", sep = "\n")
>>> Hasan
		Alp
		Doyduk

#çıktıda yıldız kullanımı (*)
#her öge arasını ifade eder
#herhangi bir parametre kullanılmadığı takdirde her öge arasına boşluk bırakılır
print(*"Python")
>>> P y t h o n

print(*"TBMM", sep = ".")
>>> T.B.M.M

#bool() içerisine yazılan sayı 0 değilse True, 0 ise False sonucu oluşur
print(bool(2))
>>> True
print(bool(0))
>>> False

a = None #değeri atanmamış değişken yaratma

#kalanı bulma operatörü
print(12 % 2)
>>> 0
print(11 % 3)
>>> 2

#range() print() ile kullanımı
print(*range(0, 10)
>>> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(*range(10)
>>> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(*range(1, 10, 2)
>>> 1, 3, 5, 7, 9
print(*range(10, 0, -1)
>>> 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

#list comprehension
list1 = [1, 2, 3, 4, 5]
list2 = [i for i in list1]
print(list2)
>>> [1, 2, 3, 4, 5]
a = Python
list3 = [i*3 for i in a]
print(list3)
>>> [PPP, yyy, ttt, hhh, ooo, nnn]
list4 = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]]
list5 = [x for i in list4 for x in i]
print(list5)
>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#return parametresi kullanılmayan fonksiyonlara void fonksiyon denir

#fonksiyonlarda varsayılan değer atama
def selam(isim = "İsimsiz"):
		print("Selam", isim)
selam()
selam(Alp)
>>> Selam İsimsiz
>>> Selam Alp

#string formatlama
name = "Hasan"
surname = "Doyduk"
print("My name is {} {}".format(name, surname))
>>> My name is Hasan Doyduk
print("My name is {1} {0}.".format(name, surname))
>>> My name is Doyduk Hasan
print("My name is {a} {b}.".format(a = name, b = surname))
>>> My name is Hasan Doyduk
result = 200 / 700
print("The result is {r:1.3}".format(r = result))
>>> The result is 0.2857142857142857
print("The result is {r:1.3}".format(r = result))
>>> The result is 0.286
print("The result is {r:1.4}".format(r = result))
>>> The result is 0.2857
print("The result is {r:10.4}".format(r = result))
>>> The result is          0.2857

#f string
name = "Hasan"
surname = "Doyduk"
print(f"My name is {name} {surname}")
>>> My name is Hasan Doyduk

#local değerle global değeri değiştirmek
a = 2
def fonk():
		global a
		a = 3
		print(a)
fonk()
print(a)
>>> 3
>>> 3

#nonlocal iç içe fonksiyonlarda önceki fonksiyonun değişkenini referans alır
def outer():
		first_num = 1
		def inner():
				nonlocal first_num
				second_num = 1
				print("inner-second_num is:", second_num)
		inner()
		print("outer-first_num is:", first_num)
outer()
>>> inner-second_num is: 1
>>> outer-first_num is: 0

#pass kelimesi bloğu daha sonra tanımlayacağını belirtmek için kullanılır
