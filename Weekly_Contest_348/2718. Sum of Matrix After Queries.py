// Brute Force Approach ----->  TLE(Time Limit Exceeded) <------- 

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        
        
        
        matrix = []
        k=0
        for i in range(n):
            liste = []
            for j in range(n):
                liste.append(0)
            matrix.append(liste)
     
     
        for values in queries:
            typ, index, value = values[0], values[1], values[2]
            if typ==0:
                for i in range(n):
                    
                    matrix[index][i]=value
                
            elif typ==1:
                for i in range(n):
                    
                    matrix[i][index]=value
               
        
        summ = 0
        for i in range(n):
            for j in range(n):
                summ+=matrix[i][j]
        return summ
