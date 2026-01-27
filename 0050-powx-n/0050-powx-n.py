class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def recurr(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = recurr(x, n//2)
            res = res * res
            if n%2 != 0:
                return res*x
            else:
                return res
        res = recurr (x, abs(n))
        if n>= 0:
            return res
        else:
            return 1/res

       
            
         
        
        
        