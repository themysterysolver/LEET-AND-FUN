class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minuteAngle=(minutes/5)*30
        percentageMoved=(minutes/5)/12*(100)
        hoursHand=((hour%12)*30)
        hoursAfterExtra=hoursHand+30*percentageMoved/100
        angle=abs(hoursAfterExtra-minuteAngle)
        print(minuteAngle,percentageMoved,hoursHand,hoursAfterExtra,angle)
        return min(angle,360-angle)