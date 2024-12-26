class UndergroundSystem:
    def __init__(self):
        self.hashC=dict()
        self.hashTravel=dict()
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.hashC[id]=(stationName,t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startTravel,time=self.hashC[id]
        if (startTravel,stationName) in self.hashTravel:
            self.hashTravel[(startTravel,stationName)].append(t-time)
        else:
            self.hashTravel[(startTravel,stationName)]=[t-time]
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.hashTravel[(startStation,endStation)]) /len(self.hashTravel[(startStation,endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)