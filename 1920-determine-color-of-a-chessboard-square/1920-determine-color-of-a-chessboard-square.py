class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        hash = {chr(ord('a')+i):i+1 for i in range(8)}
        #print(hash)
        return (hash[coordinates[0]]+int(coordinates[1]))%2 == 1