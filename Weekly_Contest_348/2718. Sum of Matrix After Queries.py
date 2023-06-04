class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        
        rows = set()
        cols = set()
        
        result = 0
        
        for values in queries[::-1]:
            types, index, value = values[0], values[1], values[2]
            if types==1:
                if index not in cols:
                    cols.add(index)
                    result+= value*(n-len(rows))
                    
                    
            else:
                if index not in rows:
                    rows.add(index)
                    result+= value*(n-len(cols))
                
        return result
        
        
