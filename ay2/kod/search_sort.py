
# LineerSearch 
#Aranan eleman fonksiyona averilir ve listedeki her elemanla sırayla karşılaştırılır. 
# Sonuç olarak eleman listede bulunursa indexi döndürülür.Bulunamazsa "Sayı listede bulunamadı"diye mesaj gönderilir.
# Zaman Karmaşıklığı: O(n) . En kötü durumda (eleman listede yoksa veya en sondaysa) listenin tamamı tek tek gezilir. 
# Alan Karmaşıklığı: O(1) . Ekstra bir veri yapısı kullanılmıyor, sadece döngü sayacı tutuluyor.

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
# Zaman Karmaşıklığı: O(log n). Her adımda arama alanı yarıya indiği için
# n elemanlı bir listede en fazla log2(n) adımda sonuca ulaşılır.
# Alan Karmaşıklığı: O(1) . Sadece iki sınır değişkeni (en_küçük, en_büyük) ve bir orta indeks tutuluyor, ekstra veri yapısı yok.

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
# Zaman Karmaşıklığı: O(n^2) . İç içe iki döngü var; her eleman için listenin geri kalanı tekrar tekrar taranıyor.
# Alan Karmaşıklığı: O(1)
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
# Her turda kalan (henüz sıralanmamış) elemanlar arasından en küçüğü bulunur
# ve sıradaki doğru pozisyona (i'inci sıraya) yerleştirilir. Bubble Sort'tan
# farklı olarak, karşılaştırma bittikten sonra tek seferde yer değiştirme  yapılır.
# Zaman Karmaşıklığı: O(n^2) .Her i için, kalan elemanlar arasında en küçüğü bulmak amacıyla iç içe bir döngü çalışıyor. 
# Toplamda yine n*n'e yakın karşılaştırma yapılıyor.

# Alan Karmaşıklığı: O(1) . Sıralama in-place yapılıyor, sadece en_küçük_index ve temp değişkenleri tutuluyor.

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

#Insertion Sort
# Liste iki parçaya ayrılmış gibi düşünülür: sıralı kısım ve sırasız kısım 
#Sırasız kısımdaki her eleman sırayla alınır, simdiki_eleman değişkeninde tutulur
#ve sıralı kısımda geriye doğru gezilerek doğru yerine yerleştirilir.
#Bu sırada simdiki_eleman'dan büyük olan elemanlar sağa kaydırılır.

# Zaman Karmaşıklığı: O(n^2) . En kötü durumda (liste tersten sıralıysa) her
# eleman, sıralı kısmın başına kadar kaydırma gerektirebilir; bu da iç içe
#döngü etkisi yaratır. En iyi durumda (liste zaten sıralıysa) O(n)'e kadar düşebilir, çünkü hiç kaydırma gerekmez.

# Alan Karmaşıklığı: O(1) . Sıralama in-place yapılıyor, sadece şimdiki_eleman ve j değişkenleri tutuluyor.
liste_4 = [45, 12, 73, 5, 11, 14, 3]

print(' ')
print('Insertion Sort')

def insertion_sort(insertion_liste):
    uzunluk = len(insertion_liste)
    for i in range(1, uzunluk):
        simdiki_eleman = insertion_liste[i]
        j = i - 1
        while j >= 0 and insertion_liste[j] > simdiki_eleman:
            insertion_liste[j + 1] = insertion_liste[j]
            j -= 1
            print(insertion_liste)
        insertion_liste[j + 1] = simdiki_eleman
        print(insertion_liste)
    return insertion_liste

print(insertion_sort(liste_4))









