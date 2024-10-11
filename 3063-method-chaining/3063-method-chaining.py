import pandas as pd
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    ans=animals.loc[animals['weight']>100,['name','weight']].sort_values(by='weight',ascending=False)
    return ans[['name']]