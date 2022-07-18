class Solution:
    def is_digit(self,s: str) -> bool:
        try:
            int(s)
        except ValueError:
            return False
        return True
    
    def clamp(self,num: int) -> int:
        MAX_INT = 2**31 -1
        MIN_INT = -1 * 2**31
        if num >= 0:
            return min(MAX_INT,num)
        return max(MIN_INT,num)
    
    def myAtoi(self, s: str) -> int:
        # step 1
        s = s.strip()
        # step 2
        sign = "Pos"
        try:
            if s[0] == '-':
                sign = "Neg"
                s = s[1:]
            elif s[0] == '+':
                sign = "Pos"
                s = s[1:]
        except IndexError:
            pass
        # step 3
        # checks
        if len(s) < 1:
            return 0
        end_idx = -1
        for idx,char in enumerate(s):
            if not self.is_digit(char):
                end_idx = idx
                break
        res = 0
        if end_idx == 0:
            pass
        else:
            res = int(s[:]) if end_idx == -1 else int(s[:end_idx])
        # step 4
        if sign == "Neg":
            return self.clamp(-1*res)
        else:
            return self.clamp(res)
                