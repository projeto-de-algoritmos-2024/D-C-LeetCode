from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(inicio, fim):
            if inicio >= fim:
                return 0

            metade = (inicio + fim) 
            c = merge_sort(inicio, metade) + merge_sort(metade + 1, fim)  

            j = metade + 1
            for i in range(inicio, metade + 1):
                while j <= fim and nums[i] > 2 * nums[j]:
                    j += 1
                c += j - (metade + 1)