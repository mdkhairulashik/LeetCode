class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left= 1
        right=x
        result = 0
        while left <= right :
            mid= left + (right - left)//2

            if mid == x // mid:
                return mid
            elif mid < x //mid:
                result = mid
                left = mid + 1
            else:
                right = mid -1
        return result

        