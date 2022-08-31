class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        trans =  {'(':')','{':'}','[':']'}
        trans = {v:k for k,v in trans.items()}
        for ch in s:
            if ch in trans.values():
                stack.append(ch)
            else:
                if len(stack)==0:
                    return False
                top = stack.pop()
                if top != trans[ch]:
                    return False
        
        if len(stack)!=0:
            return False 
        else:
            return True