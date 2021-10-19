from typing import List


def diagonalSort(M: List[List[int]]) -> List[List[int]]:
        A = [x.copy() for x in M]
        x = len(A)
        y = len(A[0])
        posicoes = {}
        for i in range(x):
            for k in range(y):
                posicoes[y * i + k + 1] = A[i][k]
        p = 1
        valores = [x + 1 for x in range(x * y)]
        if p <= (x*y)/2:
            for i in range(x):
                for k in range(0, i + 1):
                    posicao_nova = (p, i - k, k)
                    p = p + 1
                    print(posicao_nova)
        if p > (x*y)/2:
            for k in range(1, y):
                posicao_nova = (min(p, x * y), max(0, x-k), k)
                posicao_nova = (p, i - k, k)
                p = p + 1
                print(posicao_nova)
            
        print(posicoes)


            
        
mat = [[1, 2, 3, 4],[5,6, 7, 8],[9, 10, 11, 12]]
diagonalSort(mat)