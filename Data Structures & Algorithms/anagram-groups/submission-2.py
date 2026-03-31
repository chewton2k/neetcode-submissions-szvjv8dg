class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0: 
            return []

        seen = {}

        for i in range(len(strs)): 
            key = "".join(sorted(strs[i]))
            if key not in seen: 
                seen[key] = []
            seen[key].append(strs[i])

        return list(seen.values())
        