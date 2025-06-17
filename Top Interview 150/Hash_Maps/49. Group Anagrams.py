from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            sorted_word = ''.join(sorted(s))
            dic[sorted_word].append(s)
        ans = list(dic.values())
        return ans