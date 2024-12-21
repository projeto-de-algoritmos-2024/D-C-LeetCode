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

        if k < len(menores):
            return self.mediana_das_medianas(menores, k)
        elif k < len(menores) + len(pivots):
            return pivots[0]
        else:
            return self.mediana_das_medianas(maiores, k - len(menores) - len(pivots))
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        combinados = nums1 + nums2
        print(f"Arrays combinados: {combinados}")
        
        n = len(combinados)
        print(f"Tamanho total do array combinado: {n}")
        
        if n % 2 == 1:
            #impar
            print(f"ímpar: do meio.")
            return float(self.mediana_das_medianas(combinados, n // 2))
        else:
            # par
            print(f"Par: os dois do meio.")
            esquerdo = self.mediana_das_medianas(combinados, n // 2 - 1)
            direito = self.mediana_das_medianas(combinados, n // 2)
            print(f"esquerdo = {esquerdo}, direito = {direito}")
            return (esquerdo + direito) / 2.0


# Testando
solucao = Solution()
nums1 = [1, 3]
nums2 = [2]
print(f"Resultado: {solucao.findMedianSortedArrays(nums1, nums2)}")
