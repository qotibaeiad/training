class Solution(object):
    def numDecodings(self, s):
        mapping = {}
        current_char = 'A'
        current_code_point = ord('A')
        for i in range(26):
            mapping[current_code_point - 64] = current_char
            current_code_point += 1
            current_char = chr(current_code_point)
        for item in mapping.items():
            print(item)
solution = Solution()
solution.numDecodings("123")
