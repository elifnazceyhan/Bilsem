def bilgilerigoster(ad,soyad,no,adres,tel):
    print("Adınız" ,ad)
    print("soyadınız", soyad)
    print("numaranız", no)
    print("adresiniz", adres)
    print("Telefonunuz", tel)
name=input("adınızı girin:")
surname=input("soyadınızı girin:")
number=int(input("numaranızı girin:"))
adress=input("adresinizi girin:")
telephone=int(input("telefonunuzu girin:"))
bilgilerigoster(ad=name ,soyad=surname, no=number,adres=adress, tel=telephone)
