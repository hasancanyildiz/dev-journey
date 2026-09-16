class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        # İlk pencere
        count = sum(char in vowels for char in s[:k])
        max_count = count

        # Pencereyi kaydır
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1

            if s[i] in vowels:
                count += 1

            max_count = max(max_count, count)

        return max_count
