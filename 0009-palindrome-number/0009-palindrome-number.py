class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        s1=s[::-1]
        s2=(s)
        if s2==s1:
            return True
        else:
            return False