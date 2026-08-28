# LeetCode 2769 - Find the Maximum Achievable Number
# https://leetcode.com/problems/find-the-maximum-achievable-number/
#
# Zaman Karmaşıklığı: O(1) - sabit sayıda aritmetik işlem yapılıyor
# Alan Karmaşıklığı: O(1) - ekstra veri yapısı kullanılmıyor

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        output = num + 2 * t
        return output
