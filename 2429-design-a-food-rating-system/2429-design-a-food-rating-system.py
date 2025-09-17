# Goat arjun!
# idea is to use while loop to calculate the redunant or old data!
# simply brilliant!!
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodRating = dict()
        self.foodToCusine = dict()
        self.cusine = defaultdict(list)
        for i in range(len(foods)):
            self.foodRating[foods[i]] = ratings[i]
            self.foodToCusine[foods[i]] = cuisines[i]
            #print(cuisines[i])
            #print(self.cusine[cuisines[i]])
            heapq.heappush(self.cusine[cuisines[i]],(-1*self.foodRating[foods[i]],foods[i]))
            #print(self.foodRating)
            #print(self.foodToCusine)
            #print(self.cusine)
            #print('--------------')
    def changeRating(self, food: str, newRating: int) -> None:
        c = self.foodToCusine[food]
        self.foodRating[food] = newRating
        heapq.heappush(self.cusine[c],(-1*self.foodRating[food],food))

    def highestRated(self, cuisine: str) -> str:
        while self.cusine[cuisine][0][0]!=self.foodRating[self.cusine[cuisine][0][1]]*-1:
            heapq.heappop(self.cusine[cuisine])
        return self.cusine[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)