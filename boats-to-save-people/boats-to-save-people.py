class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        first=0
        last=len(people)-1
        boats=0
        while(first<=last):
            if people[first]+people[last]<=limit:
                boats+=1
                first+=1
                last-=1
            elif people[last]<=limit:
                boats+=1
                last-=1
            else:
                return -1
        return boats
                
        
