from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(inicio, fim):
            if inicio >= fim:
                return 0

            metade = (inicio + fim) // 2
            c = merge_sort(inicio, metade) + merge_sort(metade + 1, fim)

            j = metade + 1
            for i in range(inicio, metade + 1):
                while j <= fim and nums[i] > 2 * nums[j]:
                    j += 1
                c += j - (metade + 1)

            vetor_aux = []
            i, j = inicio, metade + 1
            while i <= metade and j <= fim:
                if nums[i] <= nums[j]:
                    vetor_aux.append(nums[i])
                    i += 1
                else:
                    vetor_aux.append(nums[j])
                    j += 1

            if i <= metade:
                vetor_aux.extend(nums[i:metade + 1])
            if j <= fim:
                vetor_aux.extend(nums[j:fim + 1])

            nums[inicio:fim + 1] = vetor_aux

            return c

        return merge_sort(0, len(nums) - 1)
