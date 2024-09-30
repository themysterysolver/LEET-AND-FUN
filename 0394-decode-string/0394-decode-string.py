class Solution:
    def decodeString(self, s: str) -> str:
        result=""
        string_stack=[]
        number_stack=[]
        i=0
        while i<(len(s)):
            reverse=""
            if str(s[i]).isnumeric():
                j=i+1
                num=int(s[i])
                while str(s[j]).isnumeric():
                    num=(10*num)+int(s[j])
                    j+=1
                print('ans',s[j])
                i=j
                number_stack.append(num)
                continue
            elif s[i]==']':
                while string_stack[-1]!='[':
                    reverse=string_stack.pop()+reverse
                string_stack.pop()
                string_stack.append(reverse*number_stack.pop())
            else:
                string_stack.append(s[i])
            i+=1
            print(string_stack)
            print(number_stack)
            print('---------------------------------')
        while string_stack:
            result=result+string_stack.pop(0)
        return result

                
        