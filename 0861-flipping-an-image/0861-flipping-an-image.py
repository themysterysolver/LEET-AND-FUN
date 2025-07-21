class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            for j in range(len(image)):
                image[i][j] = 1 if image[i][j] == 0 else 0
            image[i]=image[i][::-1]
        return image