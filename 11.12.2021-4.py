#Kullanıcıdan 5 tane isim alarak kullanıcıya sorup z den a ya ya da a dan z ye sıralayınız.
liste=[]
for i in range (5):
    isim=(input ("İsim giriniz"))
    liste.append(isim)
a=(input ("A dan Z ye mi yoksa Z den A ya mı sıralansın")).upper()
if a=="A-Z":
    liste.sort()
    print(liste)
else:
    liste.sort(reverse=True)
    print(liste)













