#fonksiyonlara parametre olarak *args girerek esnek sayıda parametre girilir
def fonksiyon(*args): #istediğimiz sayıda argüman gönderebiliyoruz
    print(args)
    for i in args:
        print(i)
fonksiyon(1,2,3) 
(1, 2, 3)
>>> 1
>>> 2
>>> 3
def fonksiyon(isim,*args): 
    print("İsim:",isim)
    for i in args:
        print(i)
fonksiyon("Murat",1,2,3,4,5)
>>> İsim: Murat
>>> 1
>>> 2
>>> 3
>>> 4
>>> 5

#fonksiyonlara parametre olarak **kwargs girerek esnek sayıda ikili parametre girilir
def fonksiyon(**kwargs):
    print(kwargs)
fonksiyon(isim = "Murat", soyisim = "Coşkun", numara = 12345)
>>> {'isim': 'Murat', 'soyisim': 'Coşkun', 'numara': 12345}

#fonksiyonları return ile döndürmek
def fonksiyon(işlem_adı):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def çarpma(*args):
        çarpım = 1
        for i in args:
            çarpım *= i
        return çarpım
    if işlem_adı == "toplama":
        return toplama
    else:
        return çarpma
deneme = fonksiyon("toplama")
deneme(1,2,3,4,5,6,7)
>>> 28
deneme2 = fonksiyon("çarpma")
deneme2(1,2,3,4,5,6,7,8,9)
>>> 362880 

#fonskiyonları parametre olarak gönderme
def toplama(a,b):
    return a + b
def çıkarma(a,b):
    return a-b
def çarpma(a,b):
    return a * b
def bölme(a,b):
    return a / b
def anafonksiyon(func1,func2,func3,func4,işlem_adı):
    if (işlem_adı == "toplama"):
        print(func1(3,4))
    elif (işlem_adı == "çıkarma"):
        print(func2(10,3))
    elif (işlem_adı == "çarpma"):
        print(func3(10,3))
    elif (işlem_adı == "bölme"):
        print(func4(10,4))
    else:
        print("Geçersiz işlem adı...")
anafonksiyon(toplama,çıkarma,çarpma,bölme,"toplama")
>>> 7
anafonksiyon(toplama,çıkarma,çarpma,bölme,"bölme")
>>> 2.5

#decorator fonksiyon kullanmadan
import time
def kareleri_hesapla(sayılar):
    sonuç = []
    baslama = time.time()
    for i in sayılar:
        sonuç.append(i ** 2)
		bitis = time.time()
    print("Bu fonksiyon " + str(bitis - baslama) + " saniye sürdü.") 
def küpleri_hesapla(sayılar):
    sonuç = []
    baslama = time.time()
    for i in sayılar:
        sonuç.append(i ** 3)
			bitis = time.time()
    print("Bu fonksiyon " + str(bitis - baslama) + " saniye sürdü.")
kareleri_hesapla(range(100000))
küpleri_hesapla(range(100000))
>>> Bu fonksiyon 0.14309906959533691 saniye sürdü.
>>> Bu fonksiyon 0.1360929012298584 saniye sürdü.

#decorator fonksiyon kullanarak
import time
def zaman_hesapla(fonksiyon):
    def wrapper(sayılar):
        baslama = time.time()
        sonuç =  fonksiyon(sayılar)
        bitis =  time.time()
        print(fonksiyon.__name__ + " " + str(bitis-baslama) + " saniye sürdü.")
        return sonuç
    return wrapper 
@zaman_hesapla
def kareleri_hesapla(sayılar):
    sonuç = []
    for i in sayılar:
        sonuç.append(i ** 2)
    return sonuç
@zaman_hesapla
def küpleri_hesapla(sayılar):
    sonuç = []
    for i in sayılar:
	       sonuç.append(i ** 3)
    return sonuç
kareleri_hesapla(range(100000))
küpleri_hesapla(range(100000))
>>> kareleri_hesapla 0.1340925693511963 saniye sürdü.
>>> küpleri_hesapla 0.13509273529052734 saniye sürdü.
