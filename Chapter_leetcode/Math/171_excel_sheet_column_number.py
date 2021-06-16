def titleToNumber(s):
    res = 0
    val = [i for i in range(1, 27)]
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    d = dict(zip(letters, val))
    for ch in s:
        res = res * 26 + d[ch]
    return res


#res=0
# for digit in '67':
#     res=res * 10 + int(digit)
#     print(res)

# def str2num(s):
#     res = 0
#     for digit in s:
#         res = res * 10 + int(digit)
#     return res


# class Solution:
#     def titleToNumber(self, columnTitle: str) -> int:
#         res = 0
#         val = [i for i in range(1, 27)]
#         letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#         d = dict(zip(letters, val))
#         for ch in columnTitle:
#             res = res * 26 + d[ch]
#         return res