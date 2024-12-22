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

        z0 = self.karatsuba(x0, y0)  
        z2 = self.karatsuba(x1, y1)  
        z1 = self.karatsuba(str(int(x0) + int(x1)), str(int(y0) + int(y1))) 

        middle = str(int(z1) - int(z2) - int(z0))
        
        return str(int(z2 + '0' * (2 * metade)) + int(middle + '0' * metade) + int(z0))

teste = Solution()
print(teste.multiply("1234", "5678")) 