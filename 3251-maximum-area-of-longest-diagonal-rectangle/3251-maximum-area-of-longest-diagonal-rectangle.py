class Solution:
    def areaOfMaxDiagonal(self, d: List[List[int]]) -> int:
        m=0
        a=0
        for i ,j in d:
            if m<((i**2)+(j**2))**0.5:
                m=((i**2)+(j**2))**0.5
                a=i*j
            elif m==((i**2)+(j**2))**0.5:
                a=max(a,i*j)
        return a