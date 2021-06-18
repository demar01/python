import string

alphabet = string.ascii_uppercase

class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""

        while n > 0:
            n -= 1

            n, i = divmod(n, 26)
            result += alphabet[i]

        return result[::-1]