class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        parent = [i for i in range(n+1)]

        def find(parent , node):
            if parent[node]==node:
                return node
            return find(parent, parent[node])

        count = 0
        for edge in connections:
            u = edge[0]
            v = edge[1]

            parent_of_u = find(parent , u)
            parent_of_v = find(parent, v)

            if parent_of_u!=parent_of_v:
                parent[parent_of_v] = parent_of_u
                count+=1

        return n-1-count
