class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        def display():
            for row in events:
                print(row)
            print('------------')
        events=sorted(events,key=lambda x:(int(x[1]),-1*ord(x[0][0])))
        display()
        mentions=[0]*numberOfUsers
        interval = {i:[0,0] for i in range(numberOfUsers)}
        for type,time,id in events:
           
            if type=="OFFLINE":
                interval[int(id)] = [int(time),int(time)+60]
            else:
                if id=="ALL":
                    for i in range(numberOfUsers):
                        mentions[i]+=1
                elif id=="HERE":
                    for id,(s,e) in interval.items():
                        if not s<=int(time)<e:
                            mentions[id]+=1
                else:
                    ids=re.findall(r'\d+',id)
                    ids=list(map(int,ids))
                    for i in ids:
                        mentions[i]+=1
            #print(mentions)
            #print(interval)
            #print('-----------------')
        return mentions
                    
                
            