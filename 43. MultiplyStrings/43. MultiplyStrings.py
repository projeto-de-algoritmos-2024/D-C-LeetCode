class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        return self.karatsuba(num1, num2)

    def karatsuba(self, num1: str, num2: str) -> str:
        if len(num1) < 10 or len(num2) < 10:
            return str(int(num1) * int(num2))

        tamanhoMax = max(len(num1), len(num2))
        metade = tamanhoMax // 2
        
        num1, num2 = num1.zfill(tamanhoMax), num2.zfill(tamanhoMax)  
        
        x1, x0 = num1[:-metade], num1[-metade:]  
        y1, y0 = num2[:-metade], num2[-metade:]  
        
        print(f"Dividido num1: {num1} -> x1: {x1}, x0: {x0}")
        print(f"Dividido num2: {num2} -> y1: {y1}, y0: {y0}")
        
        return "Produto intermediario"

sol = Solution()

print("Resultado para '1234' e '5678':")
print(sol.multiply("1234", "5678"))