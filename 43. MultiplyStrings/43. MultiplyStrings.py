class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        num1_bin = bin(int(num1))[2:] 
        num2_bin = bin(int(num2))[2:]  

        result_bin = self.karatsuba(num1_bin, num2_bin)

        return str(int(result_bin, 2))

    def karatsuba(self, num1: str, num2: str) -> str:
        if len(num1) < 10 or len(num2) < 10:
            return bin(int(num1, 2) * int(num2, 2))[2:]

        tamanhoMax = max(len(num1), len(num2))
        metade = tamanhoMax // 2
        
        num1, num2 = num1.zfill(tamanhoMax), num2.zfill(tamanhoMax) 
        x1, x0 = num1[:-metade], num1[-metade:]
        y1, y0 = num2[:-metade], num2[-metade:]

        z0 = self.karatsuba(x0, y0)  
        z2 = self.karatsuba(x1, y1)  
        z1 = self.karatsuba(self.soma_binaria(x0, x1), self.soma_binaria(y0, y1)) 

        middle = self.subtracao_binaria(self.subtracao_binaria(z1, z2), z0)
        
        result = self.soma_binaria(self.soma_binaria(z2 + '0' * (2 * metade), middle + '0' * metade), z0)
        return result

    def soma_binaria(self, bin1: str, bin2: str) -> str:
        return bin(int(bin1, 2) + int(bin2, 2))[2:]

    def subtracao_binaria(self, bin1: str, bin2: str) -> str:
        return bin(max(0, int(bin1, 2) - int(bin2, 2)))[2:]
