class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        orginal=[0]
        for i in range(len(derived)):
            orginal.append(orginal[i]^derived[i])
        if orginal[0]==orginal[-1]:
            return True
        orginal=[1]
        for i in range(len(derived)):
            orginal.append(orginal[i]^derived[i])
        if orginal[0]==orginal[-1]:
            return True
        return False