class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for item in strs:
            dic[tuple(sorted(item))].append(item)
        return list(dic.values())