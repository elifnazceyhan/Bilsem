# w kipi dosya yoksa yeniden oluşturur,var ise eskiyi silip yeniden oluşturur.
dosya=open("bilgiler.txt","w",encoding="utf 8")
dosya.write("merhaba\n")
dosya.write("15.01.2022 saat 13.05te giriş yapıldı.\n")
dosya.close()
