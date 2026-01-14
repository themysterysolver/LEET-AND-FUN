class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def compute_area(mid,squares):
            area_below,area_above=0,0
            for x,y,l in squares:
                top=y+l
                if top<=mid:
                    area_below+=l*l
                elif y>=mid:
                    area_above+=l*l
                else:
                    hb=mid-y
                    area_below+=l*hb
                    ha=top-mid
                    area_above+=l*ha
            return area_below,area_above
        y_values=set()
        for x,y,l in squares:
            y_values.add(y)
            y_values.add(y+l)
        low,high=min(y_values),max(y_values)
        while abs(high-low)>1e-6:
            mid=(high+low)/2
            area_below,area_above=compute_area(mid, squares)
            if area_below<area_above:
                low = mid
            else:
                high = mid
        return round(low,5)
            