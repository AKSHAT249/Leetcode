class Solution:
    def sortString(self, s: str) -> str:
        hashmap = {}
        for letter in s:
            if letter not in hashmap:
                hashmap[letter] = 1
            else:
                hashmap[letter] += 1
        
        result = ""

        frequency_count = 0 

        while result != len(s) and frequency_count !=len(hashmap):
            for i in range(97, 123):
                if chr(i) in hashmap and hashmap[chr(i)]>0:
                    result += chr(i)
                    hashmap[chr(i)]-=1
                    if hashmap[chr(i)]==0:
                        frequency_count +=1

           
            for i in range(122, 96, -1):
                if chr(i) in hashmap and hashmap[chr(i)]>0:
                    result += chr(i)
                    hashmap[chr(i)]-=1
                    if hashmap[chr(i)]==0:
                        frequency_count +=1
                
        return result
