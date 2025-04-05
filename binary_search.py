class Solution:

    def binary_search(self, ds:list | str, element:int | float | str):
        from math import ceil

        l:int = 0
        r:int = len(ds) - 1
        
        while True:
            middle = ds[ceil(len(ds[l:r]) / 2) + l]

            if middle == element or l == element or r == element:
                return True
            
            elif l == r - 1:
                return False
            
            else:

                if middle == element or l == element or r == element:
                    continue
                
                elif middle < element:
                    l = ds.index(middle) + 1

                elif middle > element:
                    r = ds.index(middle) - 1

sol = Solution()

from random import randint

array = [randint(0, 100) for num in range(11)]
array.sort()
print(sol.binary_search(array, 33))