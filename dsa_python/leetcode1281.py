class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        pro=0

        while n>0:
            d=n%10
            sum =+d
            pro *=d
            d//=10

        return sum-pro

