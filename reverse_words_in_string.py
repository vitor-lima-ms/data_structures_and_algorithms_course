"""Minha solução"""
# string = input("Digite uma string: ").split()

# res = ''
# for word in string:
#     if len(string) == 1:
#         res = string[0][::-1]
#         break
#     else:
#         if string.index(word) == -1:
#             res += word[::-1]
#         res += word[::-1] + ' '

# print(res)

"""Solução do prof"""
class Solution:
    def reverse_words(self, string):
        l, r = int(), int()
        res = str()

        while r < len(string):
            if string[r] != ' ':
                r += 1
            else:
                res += string[l:r][::-1] + ' '
                r += 1
                l = r
    
        res += string[l:r + 2] # Como paramos no r < len(string), precisamos incrementar 1 + 1
        return res
    
sol = Solution()
print(sol.reverse_words('car art'))