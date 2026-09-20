class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:

            # Kabın alanını hesapla
            area = min(height[left], height[right]) * (right - left)

            # En büyük alanı güncelle
            max_area = max(max_area, area)

            # Küçük olan tarafı hareket ettir
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

