class Solution:
    def smallestNumber(self, num: int) -> int:
        if num<=0:
            new_num=list(str(num))
            new_num.sort(reverse=True)
            new_num.insert(0,new_num.pop())
            return int(''.join(new_num))
        new_num=list(str(num))
        new_num.sort()
        if new_num[0]=='0':
            for i in range(len(new_num)):
                if new_num[i]!='0':
                    new_num[0],new_num[i]=new_num[i],new_num[0]
                    break
        print(new_num)
        return int(''.join(new_num))

        