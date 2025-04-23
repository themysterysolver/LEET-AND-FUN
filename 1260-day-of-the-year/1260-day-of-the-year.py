class Solution:
    def dayOfYear(self, date: str) -> int:
        def is_leap_year(yr):
            return (yr%4==0 and yr%100!=0) or (yr%400==0)
        monthsWithoutLeapYear=[31,28,31,30,31,30,31,31,30,31,30,31]
        monthsWithLeapYear=[31,29,31,30,31,30,31,31,30,31,30,31]
        year=int(date[:4])
        #print(is_leap_year(year))
        count=0
        if not is_leap_year(year):
            for i in range(int(date[5:7])-1):
                count+=monthsWithoutLeapYear[i]
            count+=int(date[8:])
        else:
            for i in range(int(date[5:7])-1):
                count+=monthsWithLeapYear[i]
            count+=int(date[8:])
        return count