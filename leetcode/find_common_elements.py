from typing import List

# LeetCode 2956 - Find Common Elements Between Two Arrays
# https://leetcode.com/problems/find-common-elements-between-two-arrays/
#
# Zaman Karmaşıklığı: O(n*m) "num in nums2" ve "num in nums1" kontrolleri
# liste üzerinde doğrusal arama yaptığı için, dıştaki döngü ile birleşince
# toplamda n*m'e yakın bir karmaşıklık oluşuyor.
# Alan Karmaşıklığı: O(1) girdi boyutundan bağımsız, sadece iki sayaç
# değişkeni ve sonuç listesi tutuluyor.


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer1 = 0
        answer2 = 0

        for num in nums1:
            if num in nums2:
                answer1 += 1

        for num in nums2:
            if num in nums1:
                answer2 += 1

        return [answer1, answer2]
