'''
Kullanıcıdan negatif bir sayı girmesini isteyin,pozitif sayı girene kadar tekrar etsin
'''
sayi=int(input("Bir negatif sayı gir"))
while sayi<0:
    print (int(input ("Bir negatif sayı gir")))
    while sayi>0:
        print("-")
