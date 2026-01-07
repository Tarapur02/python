class Solution:
    def countOdds(self, low: int, high: int) -> int:

        return (high+1)//2-(low)//2
    

low=3
high=7

viresh=Solution()
print(viresh.countOdds(low,high))
                
        