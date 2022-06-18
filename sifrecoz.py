from cryptography.fernet import Fernet

def keyUret():
    key = Fernet.generate_key()
    with open("key.txt", "wb") as file:
        file.write(key)


def dosyaAc(dosya):
    with open(dosya,"rb") as dosyam:
        return dosyam.read()
    print(key)    
key = dosyaAc("key.txt")



def sifrecoz (dosya,key):
    f=Fernet(key)
    sifreli=f.decrypt(dosyaAc(dosya))
    with open(dosya, "wb")as sifrecoz:
        sifrecoz.write(sifreli)
sifrecoz ("galileo.jpg",key )    


