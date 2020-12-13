class Solution:
    def candy(self, ratings: List[int]) -> int:
        cc=0
        candies=[1]*len(ratings)
        for i in range(len(candies)-1):
            if ratings[i+1]>ratings[i]:
                if candies[i+1]<=candies[i]:
                    candies[i+1] = candies[i]+1
                
        for i in range(len(candies)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                if candies[i]<=candies[i+1]:
                    candies[i] = candies[i+1]+1
        return sum(candies)
        
