class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs: 
            result += string + "0x30"
        return result

    def decode(self, s: str) -> List[str]:

        result = s.split("0x30")[:-1]
        return result