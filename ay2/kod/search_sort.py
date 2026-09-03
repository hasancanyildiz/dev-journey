
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



# BinarySearch
# İlk olarak aranan elaman ,sıralı listenin ortasındaki elemanla karşılaştırırlır
# Aranan eleman ortadaki elemandan küçükse listenin sol yarısına, büyükse sağ yarısına geçilir.
# Bu işlem eleman bulunana veya aranacak alan kalmayana kadar devam eder.
# Eleman bulunursa indexi döndürülür. Bulunamazsa "Sayı bulunamadı" mesajı gönderilir.

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


#Bubble Sort
# Liste baştan sona gezilir, yan yana duran iki eleman karşılaştırılır.
# Soldaki eleman sağdakinden büyükse yerleri değiştirilir (swap).
# Bu işlem her turda tekrarlanır; her turun sonunda o ana kadarki en büyük eleman listenin sonuna doğru "yükselmiş" olur.
# Liste tamamen sıralanana kadar bu turlar devam eder.
print(' ')
print('Bubble Sort')
liste_2=[45,12,73,5,11,14,3]

def bubble_sort (bubble_list):
    uzunluk=len (bubble_list)
    for i in range (uzunluk):
        counter=uzunluk-1 
        for j in range (counter):
            if bubble_list[j]>bubble_list[j+1]:
                temp =bubble_list[j]
                bubble_list[j] =bubble_list[j+1]
                bubble_list[j+1]=temp
                print(bubble_list)

    return bubble_list          

print(bubble_sort(liste_2))

#Selection Sort
print(' ')
print('Selection Sort')

liste_3=[45,12,73,5,11,14,3]

def selection_sort (selection_liste):
    uzunluk=len (selection_liste)
    for i in range (uzunluk):
        en_küçük_index =i
        for j in range(i,uzunluk):
            if selection_liste[en_küçük_index]> selection_liste[j]:
                en_küçük_index  =j
        temp =selection_liste[en_küçük_index]
        selection_liste[en_küçük_index] =selection_liste[i]
        selection_liste[i]=temp
        print(selection_liste)
    return selection_liste

print(selection_sort(liste_3))


        








