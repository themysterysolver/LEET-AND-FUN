class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        # print(s)
        def IPv4(s):
            s = queryIP.split('.')
            if len(s)!=4:
                return False
            for c in s:
                if not c.isdigit():
                    return False
                if not (0<=int(c)<=255):
                    return False
                if c[0] == '0' and len(c)>1:
                    return False
            return True
        def IPv6(s):
            s = s.split(':')
            if len(s)!=8:
                return False
            for c in s:
                if len(c)>4 or len(c)<1:
                    return False
                c = c.lower()
                if re.fullmatch(r'[0-9a-f]+',c):
                    continue
                else:
                    return False
            return True
        if IPv4(queryIP):
            return "IPv4"
        if IPv6(queryIP):
            return "IPv6"
        return "Neither"

