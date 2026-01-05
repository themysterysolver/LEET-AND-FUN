class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            ns = s.lower()
            idx = ns.index('@')
            return ns[0]+"*****"+ns[idx-1:]
        else:
            ns = ""
            for c in s:
                if c.isdigit():
                    ns+=c
            if len(ns) == 10:
                return "***-***-"+ns[-4:]
            if len(ns) == 11:
                return "+*-***-***-"+ns[-4:]
            if len(ns) == 12:
                return "+**-***-***-"+ns[-4:]
            if len(ns) == 13:
                return "+***-***-***-"+ns[-4:]