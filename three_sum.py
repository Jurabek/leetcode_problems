class Solution(object):
    def add_three_numbers(self, numbers, target):
        length = len(numbers)
        for i in range(0, length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if(numbers[i] + numbers[j] + numbers[k] == target):
                        return [i, j, k]
        
        return -1;

solution = Solution()
result = solution.add_three_numbers([3, 4, 7, 10, 12, 4, 6], 21)

print(result)