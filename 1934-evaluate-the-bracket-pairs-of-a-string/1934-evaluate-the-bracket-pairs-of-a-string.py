class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        
        result = ''
        hash = dict()
        for k,v in knowledge:
            hash[k] = v
        
        seen = False
        char = ''
        for c in s:
            if seen:
                if c == ')':
                    if char in hash:
                        result+=hash[char]
                    else:
                        result+='?'
                    char = ''
                    seen = False
                else:
                    char+=c
            else:
                if c == '(':
                    seen =True
                else:
                    result+=c
        return result
