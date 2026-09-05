from typing import List

# LeetCode 2517 - Maximum Tastiness of Candy Basket
# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/
#
# Cevap üzerinde binary search yapılıyor: aranan şey listede bir eleman değil,
# mümkün olan en büyük "minimum fark" değeri. Fiyatlar sıralanır, sonra
# 0 ile (en pahalı - en ucuz) arasında binary search yapılır. Her adayda
# (orta), sıralı fiyatlar gezilerek greedy şekilde kaç şeker seçilebileceği
# sayılır (bir şeker, öncekinden en az "orta" kadar uzaksa seçilir).
# k tane seçilebiliyorsa bu fark mümkündür, daha büyüğü denenir.
# Seçilemiyorsa daha küçüğü denenir.
#
# Zaman Karmaşıklığı: O(n log n) - Sıralama O(n log n); binary search
#   O(log(en_büyük_fark)) adım atar, her adımda O(n) sürede sayım yapılır.
# Alan Karmaşıklığı: O(1) - Sıralama hariç ekstra veri yapısı kullanılmıyor.

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        en_küçük = 0
        en_büyük = price[-1] - price[0]
        while en_küçük <= en_büyük:
            orta = (en_küçük + en_büyük) // 2
            sayac = 1
            son_secilen = price[0]
            for i in range(1, len(price)):
                if price[i] - son_secilen >= orta:
                    sayac += 1
                    son_secilen = price[i]
            if sayac >= k:
                en_küçük = orta + 1
            else:
                en_büyük = orta - 1
        return en_büyük

