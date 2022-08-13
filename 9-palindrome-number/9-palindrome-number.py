class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0 and x!=0:
            return False
        reversed_number = 0
        while x > reversed_number:
            reversed_number = x%10 + reversed_number * 10
            x = x//10
        if x == reversed_number or x == reversed_number//10:
            return True
        return False