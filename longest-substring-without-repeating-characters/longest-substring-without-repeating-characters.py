class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs_len = []
        if len(s)<1:
            return 0
        for i,char_1 in enumerate(s):
            sub = char_1
            for j,char_2 in enumerate(s[i+1:]):
                if char_2 not in sub:
                    sub = sub + char_2
                else:
                    break
            print(sub)
            subs_len.append(len(sub))
        return max(subs_len)