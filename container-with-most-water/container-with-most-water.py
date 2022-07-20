class Solution:
    def maxArea1(self, height: List[int]) -> int:
        max_area = 0
        for left in range(len(height)):
            for right in range(left+1,len(height)):
                area = (right-left) * (min(height[left],height[right]))
                max_area = max(max_area,area)
        return max_area
    
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            ans = (right-left) * (min(height[left],height[right]))
            max_area = max(max_area,ans)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_area
        
    
    
        