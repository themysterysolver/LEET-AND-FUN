class Solution:
    def minSteps(self, n: int) -> int:
        copy=0
        clipboard=1
        operation=0
        print('cl,co,op')
        print(clipboard,copy,operation)
        while clipboard!=n:
            if n%clipboard==0:
                copy=clipboard
                operation+=1
            clipboard+=copy
            operation+=1
            print(clipboard,copy,operation)
        return operation