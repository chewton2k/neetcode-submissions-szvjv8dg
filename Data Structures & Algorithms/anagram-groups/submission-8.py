class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for st in strs:
            key = ''.join(sorted(st))
            res[key].append(st)



        return list(res.values())

            