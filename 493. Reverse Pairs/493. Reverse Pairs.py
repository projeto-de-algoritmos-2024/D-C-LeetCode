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

            sorted_nums = []
            i, j = inicio, metade + 1
            while i <= metade and j <= fim:
                if nums[i] <= nums[j]:
                    sorted_nums.append(nums[i])
                    i += 1
                else:
                    sorted_nums.append(nums[j])
                    j += 1

            if i <= metade:
                sorted_nums.extend(nums[i:metade + 1])
            if j <= fim:
                sorted_nums.extend(nums[j:fim + 1])

            nums[inicio:fim + 1] = sorted_nums

            return c

        return merge_sort(0, len(nums) - 1)

test_nums = [1,3,2,3,1]
solution = Solution()
result = solution.reversePairs(test_nums)
print(result)
