#bin() fonksiyonu bir sayıyı ikilik tabana çevirmek için kullanılır
print(bin(4))
>>> 0b100
print(bin(19)) 
>>> 0b10011
print(bin(521))
>>> 0b1000001001

#hex() fonksiyonu bir sayıyı 16'lık tabana çevirmek için kullanılır
print(hex(32)) #sayımız 16'lık tabanda yazıldı
>>> 0x20
print(hex(54)) #sayımız 16'lık tabanda yazıldı
>>> 0x36
print(hex(1212)) #sayımız 16'lık tabanda yazıldı
>>> 0x4bc

#abs fonksiyonu sayının mutlak değerini almamızı sağlar
print(abs(-4))
>>> 4
print(abs(4.5))
>>> 4.5

#round fonksiyonu sayıları alta veya üste yuvarlar
print(round(3.7))
>>> 4
print(round(3.2))
>>> 3
print(round(3.21329321321323,4)) #ondalıklı sayının 4. hanesine göre yuvarlar
>>> 3.2133
print(round(3.21329321321323,3)) #ondalıklı sayının 3. hanesine göre yuvarlar
>>> 3.2133

#max() fonksiyonu verdiğimiz değerlerin en büyüğünü döndürür
#min() fonksiyonu verdiğimiz değerlerin en küçüğünü döndürür
#sayıları liste veya demet şeklinde de verebiliriz

#sum() fonksiyonu verilen değerleri toplayarak döndürür
print(sum([3,4,5,6,7]))
>>> 25
print(sum((3,4)))
>>> 7
#değerlerin liste veya demet şeklinde verilmesi gerekir

#pow() fonksiyonu üs alma işlemlerinde kullanılır
print(pow(2,4)) #2 üzeri 4
>>> 16
print(pow(17,2)) #17 üzeri 2
>>> 289
