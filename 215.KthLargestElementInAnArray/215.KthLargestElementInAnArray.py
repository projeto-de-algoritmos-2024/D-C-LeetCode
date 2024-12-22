from typing import List

class Solution:
    def mediana_das_medianas(self, A: List[int], k: int) -> int:
        print(f"Entrada para mediana_das_medianas: A = {A}, k = {k}")
        
        # A tem 5 ou menos elementos
        if len(A) <= 5:
            A.sort()
            print(f"Array pequeno ordenado: {A}")
            return A[k]  
        
        # Divisao da lista para tamanho 5
        sublistas = [A[i:i + 5] for i in range(0, len(A), 5)]
        print(f"Sublistas de 5 elementos: {sublistas}")

        medianas = [sorted(sublista)[len(sublista) // 2] for sublista in sublistas]
        print(f"Medianas de cada sublista: {medianas}")

        pivo = self.mediana_das_medianas(medianas, len(medianas) // 2)
        print(f"Pivo (mediana das medianas): {pivo}")
        
        menores = [x for x in A if x < pivo]
        maiores = [x for x in A if x > pivo]
        pivots = [x for x in A if x == pivo]
        print(f"Menores: {menores}, Pivos: {pivots}, Maiores: {maiores}")

        if k < len(maiores):
            return self.mediana_das_medianas(maiores, k)
        elif k < len(maiores) + len(pivots):
            return pivots[0]
        else:
            return self.mediana_das_medianas(menores, k - len(maiores) - len(pivots))
        


# Teste 
solucao = Solution()
resultado = solucao.mediana_das_medianas([3, 2, 1, 5, 6, 4], 2)  
print(f"Resultado: {resultado}")
