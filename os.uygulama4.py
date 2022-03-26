basla=input("Bir harf yaz")
import os
for i in os.listdir():
    if i.startswith(basla):
         print(i)
