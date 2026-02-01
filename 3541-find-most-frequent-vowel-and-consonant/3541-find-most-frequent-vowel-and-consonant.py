class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = defaultdict(int)
        c = defaultdict(int)
        for i in s:
            if i in 'aeiou':
                v[i]+=1
            else:
                c[i]+=1
        return max(v.values() or [0]) + max(c.values() or [0])
