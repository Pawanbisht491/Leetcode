class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = list(pattern)
        s = s.split()
        if len(s) != len(p):
            return False

        mapPS, mapSP = {}, {}
        for c1, c2 in zip(p, s):
            if ((c1 in mapPS and mapPS[c1] != c2) or (c2 in mapSP and mapSP[c2] != c1)):
                return False
            mapPS[c1] = c2
            mapSP[c2] = c1
        return True