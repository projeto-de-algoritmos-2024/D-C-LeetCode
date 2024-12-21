class Solution:
    def multiply(self, n1: str, n2: str) -> str:
        if n1 == "0" or n2 == "0":
            return "0"
        
        return self.karatsuba(n1, n2)
    
    def karatsuba(self, n1: str, n2: str) -> str:
        return str(int(n1) * int(n2))

sol = Solution()

print(sol.multiply("0", "987654321"))