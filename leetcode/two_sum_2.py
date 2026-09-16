class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        sol = 0
        sag = len(numbers) - 1
        while sol < sag:
            toplam = numbers[sol] + numbers[sag]

            if toplam == target:
                return [sol + 1, sag + 1]

            elif toplam < target:
                sol += 1

            else:
                sag -= 1
        
