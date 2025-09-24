class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        nr,dr = abs(numerator),abs(denominator)
        sign = '-' if numerator/denominator<0 else ''
        whole = str(nr//dr)
        mod = nr%dr
        if mod == 0:
            return sign+whole
        whole+='.'
        frac = ''
        seen = dict()
        idx = 0
        while mod!=0:
            if mod in seen:
                start = seen[mod]
                return sign+whole+frac[:start]+'('+frac[start:]+')'
            seen[mod] = idx
            idx+=1
            mod*=10
            frac+=str(mod//dr)
            mod%=dr
        return sign+whole+frac
        