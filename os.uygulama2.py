#sadece txt uzantılı dosyaları ekrana yazdırınız.
import os
for i in os.listdir():
    #if ".txt" in i:
        #print(i)
     if i.endswith(".txt"):
         print(i)   
