def faktoriyel(sayi):
    sonuc=1
    for i in range(1,sayi+1):
        sonuc=sonuc*i
    print("Sayınızın faktöriyeli: ",sonuc)
no=int(input("Sayı gir"))
faktoriyel(no)
