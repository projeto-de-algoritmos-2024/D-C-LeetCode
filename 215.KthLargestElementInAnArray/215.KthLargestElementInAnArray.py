from typing import List

class Solution:
    def mediana_das_medianas(self, A: List[int], k: int) -> int:
        
        # A tem 5 ou menos elementos
        if len(A) <= 5:
            A.sort()
            return A[k]  
        
        # Divisao da lista para tamanho 5
        sublistas = [A[i:i + 5] for i in range(0, len(A), 5)]

        medianas = [sorted(sublista)[len(sublista) // 2] for sublista in sublistas]

        pivo = self.mediana_das_medianas(medianas, len(medianas) // 2)
        
        menores = [x for x in A if x < pivo]
        maiores = [x for x in A if x > pivo]
        pivots = [x for x in A if x == pivo]

        if k < len(menores):
            #busca nos menores
            return self.mediana_das_medianas(menores, k)
        elif k < len(menores) + len(pivots):
            return pivo
        else:
            #busca nos maiores
            return self.mediana_das_medianas(maiores, k - len(menores) - len(pivots))
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Arrumar o K
        k_menor = len(nums) - k 
        return self.mediana_das_medianas(nums, k_menor)
