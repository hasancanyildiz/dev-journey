
# LineerSearch 
#Aranan eleman fonksiyona averilir ve listedeki her elemanla sırayla karşılaştırılır. 
# Sonuç olarak eleman listede bulunursa indexi döndürülür.Bulunamazsa "Sayı listede bulunamadı"diye mesaj gönderilir.
liste =[1,3,5,6,8,15,70,88]

def lineerSearch(sayı):
    for i in range (len (liste)):
        if sayı == liste[i]:
            return i
    return "Sayı listede bulunamadı"

lineerSearch_indeksi=lineerSearch(5)
print(lineerSearch_indeksi)


def binarySearch (sayı):
    en_küçük =0
    en_büyük = len(liste)-1
    while en_küçük <= en_büyük :
        orta =en_küçük+ (  en_büyük-en_küçük )//2

        if sayı == liste[orta]:
            return orta

        elif sayı <liste[orta] :
            en_büyük =orta -1

        elif sayı >liste[orta] :
            en_küçük= orta +1
        
    return "Sayı bulunamadı "

binarySearch_indeksi=binarySearch(88)
print(binarySearch_indeksi)





