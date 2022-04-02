#Bilgisayardaki toplam dosya sayısını verir.
import os
sayac=0
for i in os.walk("C:/"):
    sayac=sayac+1
print(sayac)

    