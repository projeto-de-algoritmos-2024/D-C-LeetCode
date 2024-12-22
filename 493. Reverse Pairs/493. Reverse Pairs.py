from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(inicio, fim):
            if inicio >= fim:
                return 0

            metade = (inicio + fim) 
            i = merge_sort(inicio, metade) + merge_sort(metade + 1, fim)  

