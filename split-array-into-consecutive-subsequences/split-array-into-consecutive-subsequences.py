class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = collections.Counter(nums)
        end = collections.Counter()
        for i in nums:
            if not left[i]: continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
            # print(left,end,i)
        return True
#         from collections import Counter
#         frequencyCount=Counter(nums)
        
#         1->2
#         2->3
#         3->4
#         4->2
#         5->1
        
#         1,2,3
#         1,2,3
#         2,3,4
#         3,4,5
        
#         1,2,3,4,5
#         1,2,3,4
        
        
        
        
        
            
            
            
        
            
                
                
            
        
        
        
