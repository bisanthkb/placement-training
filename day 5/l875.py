class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(n,piles,h):
            total=0
            for p in piles:
                total+=math.ceil(p/m)
            if total>h:
                return False
            else:
                return True
        s,e=1,max(piles)
        while s<=e:
            m=(s+e)//2
            if can_eat(m,piles,h):
                e=m-1
            else:
                s=m+1
        return s