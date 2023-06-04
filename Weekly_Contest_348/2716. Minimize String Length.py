class Solution:
    def minimizedStringLength(self, s: str) -> int:
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]]=1
            else:
                hashmap[s[i]]+=1
        return len(hashmap)
            
        
