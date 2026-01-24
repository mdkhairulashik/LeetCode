class Solution(object):
    def lengthOfLastWord(self, k):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        k = k.strip()
        for i in range(len(k)):
          if k[i] == " ":
            l= 0
          else:
            l += 1
        return l
        
                
        