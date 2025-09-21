class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movShop = defaultdict(SortedList)
        self.rents = SortedList([])
        self.smp = dict()
        for s,m,p in entries:
            self.movShop[m].add((p,s))
            self.smp[(s,m)] = p
        
    def search(self, movie: int) -> List[int]:
        return [b for a,b in self.movShop[movie][:min(5,len(self.movShop[movie]))]]

    def rent(self, shop: int, movie: int) -> None:
        self.rents.add((self.smp[(shop,movie)],(shop,movie)))
        self.movShop[movie].remove((self.smp[(shop,movie)],shop))

    def drop(self, shop: int, movie: int) -> None:
        self.rents.remove((self.smp[(shop,movie)],(shop,movie)))
        self.movShop[movie].add((self.smp[(shop,movie)],shop))

    def report(self) -> List[List[int]]:
        return [[s,m] for p,(s,m) in self.rents[:min(5,len(self.rents))]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()