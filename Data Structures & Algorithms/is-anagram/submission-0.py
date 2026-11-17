class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self._build_dict(s) == self._build_dict(t)
       

    def _build_dict(self , curr: str) -> dict:
        counter_d= {}
        for ch in curr:
            if ch in counter_d:
              counter_d[ch] += 1
            else:
                counter_d[ch]=1
        return counter_d
        



    


        