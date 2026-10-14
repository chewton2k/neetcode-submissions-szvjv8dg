class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        seen = Counter()
        left = right = 0

        while right < len(s):
            r = s[right]
            seen[r] += 1

            while seen[r] > 1:
                l = s[left]
                seen[l] -= 1
                left += 1
            

            result = max(result, right - left + 1)
            right += 1
        return result
