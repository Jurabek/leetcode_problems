'''Given a 32-bit signed integer, reverse digits of an integer.'''

class Solution(object):
    def reverse(self, number):
        rev = 0
        while number != 0:
            rev = rev*10 + number % 10
            number = number / 10
        return rev
