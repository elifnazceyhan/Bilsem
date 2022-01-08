sayi1=int(input("Birinci sayıyı girin"))
sayi2=int(input ("İkinci sayıyı girin"))
try:
    print(sayi1/sayi2)
except ZeroDivisionError:
    print("Sayı gir dedik")

