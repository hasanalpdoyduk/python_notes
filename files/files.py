#dosya açma
open(dosya_adı,dosya_erişme_kipi)

file = open("C:/Users/user/Desktop/bilgiler.txt","w")

#dosya kapatma
file.close()

#dosyalara yazmak
file.write("...")

#encoding="utf-8" parametresini kullanarak Türkçe karakter kullanabiliyoruz
file = open("dosya_adı","w",encoding="utf-8") 

#w dosya kipi
#oluşturmak istediğimiz dizinde öyle bir dosya yoksa dosyayı oluşturuyor
#eğer öyle bir dosya varsa dosyayı silip tekrar oluşturuyor (RİSKLİ)
file = open("bilgiler.txt","w")
file = open("C:/Users/user/Desktop/bilgiler.txt","w") #depolanma yerini seçmek için
file = open("bilgiler.txt","w",encoding="utf-8") 
file.write("Mustafa Murat Coşkun")
>>> 20 #girilen içeriğin byte miktarı

#a dosya kipi
#oluşturmak istediğimiz dizinde öyle bir dosya yoksa dosyayı oluşturuyor
#eğer öyle bir dosya varsa dosyanın sonuna ekleme yapıyor
file = open("bilgiler.txt","a",encoding="utf-8")
file.write("Mustafa Murat Coşkun")
file.write("Mehmet Gençol")
file.close()
Dosya: >>> Mustafa Murat CoşkunMehmet Gençol

file = open("bilgiler.txt","a",encoding="utf-8")
file.write("Mustafa Murat Coşkun\n")
file.write("Mehmet Gençol\n")
file.close()
Dosya: >>> Mustafa Murat Coşkun
					 Mehmet Gençol

#r dosya kipi
#dosyaları okumak ve verileri almak için kullanılıyor
#zaten var olan dosyalar üzerinde uygulanır
file = open("bilgiler.txt","r",encoding="utf-8")
for i in file: 
    print(i)
file.close()
>>> Mustafa Murat Coşkun

		Mehmet Gençol

		Oğuz Artıran

		Serhat Say

		Mert Erarslan
file = open("bilgiler.txt","r",encoding="utf-8")
for i in file: 
    print(i,end = "")
file.close()
>>> Mustafa Murat Coşkun
		Mehmet Gençol
		Oğuz Artıran
		Serhat Say
		Mert Erarslan

#read() fonksiyonu ile dosya okuma
file = open("bilgiler.txt","r",encoding="utf-8")
icerik = file.read() 
print("Dosya İçeriği:") #print("Dosya İçeriği:\n",icerik,sep = "")
print(icerik)           #tek satırda yazmak için yukarıdaki kodu kullanın
file.close()
>>> Dosya İçeriği:
		Mustafa Murat Coşkun
		Mehmet Gençol
		Oğuz Artıran
		Serhat Say
		Mert Erarslan
#read() parantezi içine yazılan kadar byte veri okur

#readlines() fonksiyonu ile dosya okuma
file = open("bilgiler.txt","r",encoding="utf-8")
file.readlines()
file.close()
>>> Mustafa Murat Coşkun

#readlines() fonksiyonu ile dosya içeriğini listeye atma
file = open("bilgiler.txt","r",encoding="utf-8")
liste = file.readlines()
print(liste)
file.close()
>>> ["Mustafa Murat Coşkun\n", "Mehmet Gençol\n", "Oğuz Artıran\n", "Serhat Say\n", "Mert Erarslan\n"]

#dosyaları otomatik kapatma
with open(dosya_adı,dosya_kipi) as file:

with open("bilgiler.txt","r",encoding = "utf-8") as file:
    for i in file:
        print(i)
>>> Mustafa Murat Coşkun

		Mehmet Gençol

		Oğuz Artıran

		Serhat Say

		Mert Erarslan

#tell() fonksiyonu dosyanın gelinen yere kadar olan byte miktarını gösterir
with open("bilgiler.txt","r",encoding = "utf-8") as file:
    print(file.tell())
>>> 0

#seek() fonksiyonu içine verilen sayı kadar byte ileri gider
with open("bilgiler.txt","r",encoding = "utf-8") as file:
    file.seek(20) # 20.byte' a gelindi
    print(file.tell())
>>> 20

#r+ dosya kipi
#dosyaları okumak, verileri almak ve üzerine yazmak için kullanılıyor
#zaten var olan dosyalar üzerinde uygulanır
with open("bilgiler.txt","r+",encoding = "utf-8") as file: 
    file.seek(10)
    file.write("Deneme")
with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    print(file.read())
>>> Mustafa MuDenemeşkun
		Oğuz Artıran
		Serhat Say
		Mehmet Gençol
#dosyanın sonuna ekleme yapmak
with open("bilgiler.txt","a",encoding = "utf-8") as file:
    file.write("Mert Erarslan\n")
with open("bilgiler.txt","r",encoding = "utf-8") as file:
    print(file.read())
>>> Mustafa Murat Coşkun
		Oğuz Artıran
		Serhat Say
		Mehmet Gençol
		Mert Erarslan
#dosyanın başına ekleme yapmak
with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    icerik = "Semih Aktaş\n" + icerik
    file.seek(0)
    file.write(icerik)
with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    print(icerik)
>>> Semih Aktaş
		Mustafa Murat Coşkun
		Oğuz Artıran
		Serhat Say
		Mehmet Gençol
		Mert Erarslan
#dosyanın ortasına ekleme yapmak
with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Ahmet Baltacı\n")
    file.seek(0)
    file.writelines(liste)
with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    print(icerik)
>>> Semih Aktaş
		Mustafa Murat Coşkun
		Oğuz Artıran
		Ahmet Baltacı
		Mehmet Keper
		Serhat Say
		Mehmet Gençol
		Mert Erarslan
    
