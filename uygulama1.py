#0dan 1000e kadar olan sayıları text dosyasına yazdırınız
dosya=open("sayılar,txt","w",encoding="utf-8")
for i in range (1001):
    dosya.write(str(i)+"\n")
dosya.close()
