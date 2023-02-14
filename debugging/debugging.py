#hata ayıklama 
try:
    a = int(input("Sayı1: "))
    b = int(input("Sayı2: "))
    print(a / b) #hata burada oluşuyor, ZeroDivisionError'a bloğuna giriyoruz
except ValueError:
    print("Lütfen inputları doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")
finally:
    print("Her durumda çalışıyorum.")

#özelleşmiş hata mesajı yollama
def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen doğru bir input girin.")
    else:
        return s[::-1]
      
