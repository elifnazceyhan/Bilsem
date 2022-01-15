#Kullanıcıya adını ve kaç kere yapılmnası gerektiğini sorarak bir text dosyasına yazdırınız.
dosya=open("ad,txt","w",encoding="utf-8")
isim=input("adınız: ")
sayı=int(input("kaç kere yazılsın"))
for i in range (sayı):
    dosya.write(isim + "\n")
dosya.close()
