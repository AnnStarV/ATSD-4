# def longestPalindrome(s):
#     n = len(s)
#     if n < 2:
#         return s
#     P = [[False for _ in range(n)] for _ in range(n)]
#     longest = s[0]
#
#     # j is the length of palindrome
#     for j in range(1, n+1):
#         for i in range(n-j+1):
#             # if length is less than 3, checking s[i] == s[i+j-1] is sufficient
#             P[i][i+j-1] = s[i] == s[i+j-1] and (j < 3 or P[i+1][i+j-2])
#             if P[i][i+j-1] and j > len(longest):
#                 longest = s[i:i+j]
#     return longest
#
# print(longestPalindrome("ananakj"))

