from typing import List

class Solution:
    def mediana_das_medianas(self, A: List[int], k: int) -> int:
        print(f"Entrada para mediana_das_medianas: A = {A}, k = {k}")
        
        # A tem 5 ou menos elementos
        if len(A) <= 5:
            A.sort()
            print(f"Array pequeno ordenado: {A}")
            return A[k]  
        
        # Divisão da lista para tamanho 5
        sublistas = [A[i:i + 5] for i in range(0, len(A), 5)]
        print(f"Sublistas de 5 elementos: {sublistas}")

        medianas = [sorted(sublista)[len(sublista) // 2] for sublista in sublistas]
        print(f"Medianas de cada sublista: {medianas}")

        return self.mediana_das_medianas(medianas, len(medianas) // 2) 
#TesteMediana
solucao = Solution()
resultado = solucao.mediana_das_medianas([9, 3, 7, 2, 6, 5, 8, 1, 4, 11, 18], 2) #Ex aula
print(f"Resultado: {resultado}")