class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num=nums1+nums2
        num.sort()
        len_num = len(num)
        if len_num % 2 == 0:
            return (num [len_num//2] +num[len_num // 2 - 1]) / 2.0
        else:
            return num[len_num // 2]
               