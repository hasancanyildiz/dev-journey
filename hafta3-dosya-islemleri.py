with open("ornek.txt","w") as dosya:
    dosya.write("Merhaba dünya \n")
    dosya.write("Test dosyası. \n")
    dosya.write("Python dosya işlemleri \n")

with open("ornek.txt","r") as dosya :
    icerik = dosya.read()
    print(icerik)