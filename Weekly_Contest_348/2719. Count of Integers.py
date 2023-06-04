class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def digitSum(number):
            summ = 0
            while number:
                summ+= (number%10)
                number = number // 10
                
            return summ
        
        count = 0
        result = []
        num1 = int(num1)
        num2 = int(num2)
        for i in range(num1, num2+1):
            if i>=min_sum and i<=max_sum:
                result.append(i)
                count+=1
            else:
                if digitSum(i)>=min_sum and digitSum(i)<=max_sum:
                    result.append(i)
                    count+=1
                    
        count = count % (10**9+7)
        return count
