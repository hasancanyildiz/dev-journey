from typing import List

# LeetCode 3477 - Fruits Into Baskets II (Easy)
# https://leetcode.com/problems/fruits-into-baskets-ii/
#
# Her meyve türü için, soldan sağa doğru sepetler taranır. Kapasitesi
# meyve miktarına yetecek ilk sepet bulunduğunda, o sepet 0 yapılarak
# "kullanıldı" olarak işaretlenir (böylece bir daha seçilemez) ve meyve
# yerleştirilmiş sayılır. Hiçbir sepet uygun değilse meyve yerleştirilemez
# ve unplaced sayacı bir artırılır.
#
# Zaman Karmaşıklığı: O(n^2) - Her meyve için (n tane), en kötü durumda
#   tüm sepetler (n tane) taranabilir.
# Alan Karmaşıklığı: O(1) - Ekstra bir veri yapısı oluşturulmuyor;
#   kullanılan sepetler doğrudan baskets listesi üzerinde (0 yaparak)
#   işaretleniyor.

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0

        for fruit in fruits:
            placed = False

            for j in range(len(baskets)):
                if baskets[j] >= fruit:
                    baskets[j] = 0
                    placed = True
                    break

            if not placed:
                unplaced += 1

        return unplaced
