#datetime
from datetime import datetime
#now()
now = datetime.now()
print(now)
>>> 2022-06-04 21:30:03.737317
print(now.year)
>>> 2022
print(now.microsecond)
>>> 472991
#ctime()
print(datetime.ctime(now))
>>> Sat Jun  4 21:31:21 2022
#strftime()
print(datetime.strftime(now,"%Y"))
print(datetime.strftime(now,"%B"))
print(datetime.strftime(now,"%A"))
print(datetime.strftime(now,"%X"))
print(datetime.strftime(now,"%D"))
>>> 2022
		June
		Saturday
		21:34:14
		04/06/122
print(datetime.strftime(now,"%Y %B %A"))
>>> 2022 June Saturday
#timestamp() ve fromtimestamp()
datetime.timestamp(now)
>>> 1654367929.13533
saniye =  datetime.timestamp(now)
zaman =  datetime.fromtimestamp(saniye)
print(zaman)
>>> 2022-06-04 21:39:04.132319

tarih = datetime(2019,12,1) 
şu_an = datetime.now()
fark = tarih - şu_an
print(fark)
>>> datetime.timedelta(872, 23304, 341519)
fark.days 
>>> 872
fark.seconds 
>>> 23304

#locale
import locale
locale.setlocale(locale.LC_ALL,"")
print(datetime.strftime(now,"%Y %B %A")) #locale ile bulunduğumuz yerin diline çevirebiliyoruz
>>> 2022 Haziran Cumartesi

#os
import os
print(os.getcwd())
>>> /Users/macbookpro/PycharmProjects/Learn_Py/Udemy
#os.chdir()
os.chdir("/Users/macbookpro/PycharmProjects/Learn_Py/Udemy")
#os.listdir()
print(os.listdir())
>>> ['Udemy_Hw2_Answ4.py', '.DS_Store', 'Udemy_Hw2_Answ1.py', 'Udemy_Hw1_Answ3.py', 'Udemy_Hw1_Answ2.py', 'Udemy_Hw1_Answ1.py', 'Udemy_Hw2_Answ2.py', 'UdemyTest.py', 'Udemy_Hw2_Answ3.py']
#os.mkdir() ve os.mkdirs()
os.mkdir("Deneme1")
os.mkdirs("Deneme2/Deneme3") #Deneme2 açıldı ve Deneme2'nin içine (altına) Deneme3 açıldı
#os.rmdir() ve os.removedirs()
os.rmdir(Deneme2/Deneme3) #Deneme2'nin içindeki (altındaki) Deneme3 silindi
os.removedirs("Deneme2/Deneme3") #Deneme2 silindi ve Deneme2'nin içindeki (altındaki) Deneme3 silindi
#os.rename()
os.rename("test.txt", "text2.txt") #text.txt text2.txt olarak değiştirildi
#os.stat()
print(os.stat("text2.txt"))
print(os.stat("text2.txt").st_mtime) #değiştirilme zamanı (saniye olarak)
#os.walk()
for i in os.walk("/Users/macbookpro/Desktop"):
		print(i)
>>> #Masaüstü altındaki bütün dosyalar

for klasör_yolu, klasör_isimleri, dosya_isimleri in os.walk("/Users/macbookpro/Desktop"):
		for i in dosya_isimleri:
				if (i.endswith("txt")):
						print(i)
>>> #masaüstü altındaki dosya ismi txt bağlantısı ile biten bütün dosyalar

#sys
import sys
sys.exit() #programı durdurur
#stderr ve stdout
sys.stderr.write("Burası bir hata mesajıdır\n")
sys.stderr.flush() #buffer'ı hemen yaz
sys.stdout.write("Bu normal bir çıktıdır\n")
>>> Bu bir hata mesajıdır
		Bu normak bir çıktıdır

#request ve beautifulSoup
import requests 
from bs4 import BeautifulSoup
url =  "https://yellowpages.com.tr/ara?q=Ankara" #site linki
response =  requests.get(url) #web sayfasını çekiyor
html_icerigi = response.content  #web sayfasının içeriğini alıyor
soup =  BeautifulSoup(html_icerigi,"html.parser") #web sayfasını parçalamak için BeautifulSoup objesine atıyor
print(soup.prettify()) #daha güzel bir görüntü için prettify() fonksiyonunu kullanılıyor
>>> #web sitesinin kodu gösterilir

import requests 
from bs4 import BeautifulSoup
url =  "https://yellowpages.com.tr/ara?q=Ankara" 
response =  requests.get(url) 
html_icerigi = response.content
soup =  BeautifulSoup(html_icerigi,"html.parser")
print(soup.find_all("a")) #tüm <a> etiketlerini liste şeklinde dönüyor
>>> #web sitesinin kodundaki tüm <a> etiketleri liste şeklinde gösterilir
