#iteratorlar for döngüsü ile üzerinde gezilebilecek objelerdir
liste = [1,2,3,4,5]
iterator = iter(liste) #iter() fonksiyonu
print(next(iterator)) #next() fonksiyonu
>>> 1
print(next(iterator))
>>> 2
print(next(iterator))
>>> 3
print(next(iterator))
>>> 4
print(next(iterator)
>>> 5
print(next(iterator))
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-75-9aa5c89bf87c> in <module>()
----> 1 next(iterator) #eleman kalmadığı için "StopIteration" hatası
StopIteration:

#iterable obje oluşturmak
class Kumanda():
    def __init__(self,kanal_listesi):
        self.kanal_listesi = kanal_listesi 
        self.index = -1 
        
    def __iter__(self):
        return self 
    def __next__(self): #next fonksiyonu çağrıldığında burası çalışacak
        self.index += 1
        if (self.index < len(self.kanal_listesi)):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration
kumanda = Kumanda(["Kanal d","Trt","Atv","Fox","Bloomberg"])
iterator =  iter(kumanda) #obje iterable olduğu için iterator oluşturulabilir
print(next(iterator))
>>> Kanal d
for i in kumanda:
    print(i)
>>> Kanal d
		Trt
		Atv
		Fox
		Bloomberg

#generatorlar iterable objeler oluşturmak için kullanılan objelerdir
#değerleri istendiği zaman oluşturarak bellek tasarufu sağlar
def karelerial():
    for i in range(1,6):
        yield i ** 2 #yield anahtar kelimesi generator'un değer üretmesi için kullanılıyor
generator =  karelerial()
print(generator)
>>> <generator object karelerial at 0x0000009441354DB0>
iterator = iter(generator)
print(next(iterator))
>>> 1

#normal bir liste ile
liste = [i * 3 for i in range(5)]
prnt(liste)
>>> [0, 3, 6, 9, 12]
#generator ile 
generator = (i * 3 for i in range(5))
iterator = iter(generator)
print(next(iterator))
>>> 0
      
