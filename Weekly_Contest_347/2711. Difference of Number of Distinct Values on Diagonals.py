class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:

        def topleft(grid, i , j):
            liste = []
            i-=1
            j-=1
            while (i>=0 and i<row and j>=0 and j<column):
                if grid[i][j] not in liste:
                    liste.append(grid[i][j])

                i-=1
                j-=1

            return len(liste)


        def bottomright(grid, i , j):
            liste = []
            i+=1
            j+=1
            while (i>=0 and i<row and j>=0 and j<column):
                if grid[i][j] not in liste:
                    liste.append(grid[i][j])

                i+=1
                j+=1

            return len(liste)
                
    
        row = len(grid)
        column = len(grid[0])

        result = []

        for i in range(row):
            value = []
            for j in range(column):
                
                top_left_value = topleft(grid, i, j)
                bottom_right_value = bottomright(grid,i,j)
                print(top_left_value,bottom_right_value)
                value.append(abs(top_left_value-bottom_right_value))
            result.append(value)
        return result




