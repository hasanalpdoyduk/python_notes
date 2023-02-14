#objelerin üretileceği veri tipini yaratma
class Araba():
		model = "Renault Megane"
    renk = "Gümüş"
    beygir_gücü = 110
    silindir = 4

#obje oluşturma
araba1 = Araba()

#obje özelliklerini çağırma
araba1.model

#dir() objenin tüm özellik ve metodlarını görmeyi sağlar

#objelerin farklılaşabilmesini sağlayan __init__ fonksiyonu kullanımı
class Araba():
    def __init__(self , model = "Bilgi Yok", renk = "Bilgi Yok", beygir_gücü = 75, silindir = 4): 
        self.model =  model 
        self.renk = renk 
        self.beygir_gücü = beygir_gücü 
        self.silindir = silindir

#veri tiplerinde kalıtım
class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        print("Çalışan sınıfının bilgileri.....")
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman
class Yönetici(Çalışan):

#override (iptal) işlemi
class Yönetici(Çalışan):
    def __init__(self,isim,maaş,departman,kişi_sayısı): #sorumlu olduğu kişi sayısı
        print("Yönetici sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
        self.kişi_sayısı = kişi_sayısı #yeni eklenen özellik
    def bilgilerigoster(self):
        print("Yönetici sınıfının bilgileri.....")
        print("İsim : {} \nMaaş: {} \nDepartman: {}\nSorumlu kişi sayısı: {}".format(self.isim,self.maaş,self.departman,self.kişi_sayısı))
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı

#super kelimesi override edilen işlev veya özelliklerin bazılarını almamızı sağlar
class Yönetici(Çalışan):
    def __init__(self,isim,maaş,departman,kişi_sayısı):
        super().__init__(isim,maaş,departman) #3 tane özelliği Çalışan fonksiyonunun init fonksiyonuyla hallediyoruz
        print("Yönetici sınıfının init fonksiyonu"
        self.kişi_sayısı = kişi_sayısı
    def bilgilerigoster(self):
        print("Yönetici sınıfının bilgileri.....")
        print("İsim : {} \nMaaş: {} \nDepartman: {}\nSorumlu kişi sayısı: {}".format(self.isim,self.maaş,self.departman,self.kişi_sayısı))
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı

#özel metodlar
class Kitap():
		#__init__ metodu
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor.....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
		#__str__ metodu
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
		#__len__ metodu
    def __len__(self):
        return self.sayfa_sayısı
		#__del__ metodu
    def __del__(self):
        print("Kitap objesi siliniyor.....")

kitap1 = Kitap("İstanbul Hatırası", "Ahmet Ümit", 561, "Polisiye")

#__str__ metodu çağırılması
print(kitap1)
>>> İsim: İstanbul Hatırası
		Yazar: Ahmet Ümit
		Sayfa Sayısı: 561
		Tür: Polisiye

#__len__ metodu çağırılması
len(kitap1)
>>> 561

#__del__ metodu çağırılması
del kitap1
>>> Kitap objesi siliniyor.....
              
