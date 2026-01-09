from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)
        for string in strs:
            index = [0] * 26
            for char in string:
                index[ord(char)-ord('a')] += 1
            mapp[tuple(index)].append(string)
        return list(mapp.values())
        

        