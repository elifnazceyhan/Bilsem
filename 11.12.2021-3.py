#Kullanıcıdan 10 tane sayı alarak en büyük sayı hariç hepsini listeye ekleyen phyton kodunu yazınız.
liste=[]
for i in range (10):
    sayi1=int(input("Bir sayı girin"))
    liste.append(sayi1)
print(liste)
liste.sort()
liste.pop()
print(liste)
