from cryptography.fernet import Fernet

def keyUret():
    key = Fernet.generate_key()
    with open("key.txt", "wb") as file:
        file.write(key)
#keyUret()

def dosyaAc(dosya):
    with open(dosya,"rb") as dosyam:
        return dosyam.read()
    print(key)    
key = dosyaAc("key.txt")



def sifrele (dosya,key):
    f=Fernet(key)
    sifreli=f.encrypt(dosyaAc(dosya))
    with open(dosya, "wb")as sifrele:
        sifrele.write(sifreli)
sifrele ("galileo.jpg",key )                                                                                                                  

