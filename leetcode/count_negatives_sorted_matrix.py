from typing import List

# LeetCode 1351 - Count Negative Numbers in a Sorted Matrix
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Matrisin her satırı ve sütunu azalan sırada (non-increasing) verilmiştir.
# Bu yüzden bir satırda ilk negatif sayı bulunduğunda, o satırdaki ondan
# sonraki tüm elemanlar da negatiftir (çünkü değerler azalıyor). Bu özellik
# kullanılarak, ilk negatif bulunur bulunmaz kalan eleman sayısı kadar
# (len(grid[i]) - j) sayaç birden arttırılır ve satırın geri kalanı
# taranmadan bir sonraki satıra geçilir (break).

# Zaman Karmaşıklığı: O(m*n)
# Alan Karmaşıklığı: O(1)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    counter += len(grid[i]) - j
                    break

        return counter
