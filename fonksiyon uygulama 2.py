#Kullanıcının adını gönderdiğinizde hoşgeldin"ad" şeklinde yazsın.
ad=input("isminizi giriniz")
def isim(ad):
    print("hoşgeldin",ad)
isim(ad)

#Kendisine girilen sayının karesinin karesini hesaplayan program.
sayi=int(input("sayi giriniz: "))
def hesapla(a):
    print(a*a*a*a)
hesapla(sayi)

# fonksiyon girilen sayının çift mi tek mi old. ekrana yazsın.
def tekmi(b):
    if  b%2==0:
        print("çift")
    else:
        print("tek")
tekmi(sayi)
