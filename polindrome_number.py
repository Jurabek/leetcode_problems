class Solution(object):
    def is_polindrome_number(self, n):
        sum = 0
        temp = n
        last_number = 0
        while n != 0:
            last_number = n % 10
            sum = sum * 10 + last_number
            n = n / 10
        
        n = temp
        if(n == sum):
            return True
        else:
            return False


solution = Solution()
print(solution.is_polindrome_number(5225))