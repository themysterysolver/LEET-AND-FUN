
# Problem understanding
<!-- Describe your first thoughts on how to solve this problem. -->
- Let's understand the problem first,what they are asking is a *subsequence* of numbers which are *squares of on another* continously.
```
nums=[2,4,16,256]

```
- The longest streak is for `2` here which is `2*2(4)->4*4(16)->16*16(256)` which is `4` including `2`.
- 

---

# Approach-1:sets+sorting
# Intuition
- My idea here is to use `2-SETS` one to to store visited numbers
`visited` and our normal `nums`(given) in a set as `num_set` or `checker`.
- why `visited` ? I felt we are going to compute the same number more than once,if it is true for the smallest number say `2` in our above example then we get our ans (`4`) till `256`,then the computaion of `4`,`16` is useless.
-  Because compuation of them is always going to lead to a smaller value of `maxlen`.
- what I did is to choose an element and store it in `num` which is then *squared* each time and checked until it fails to exist in `num_set` or `checker`,while increasing `l` and adding `num*num` in `visited` to avoid future computation.
- Sorting(`sort`) is must since I am traversing from small element,because starting from a large elment and then looking for even bigger number is pointless.


# Complexity
- Time complexity:$O(N*log(N))$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:$O(N)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        nums_set=set(nums)
        visited=set([])
        print(nums)
        maxl=0
        for i in nums:
            num=i
            l=1
            while num*num in nums_set and num*num not in visited:
                visited.add(num*num)
                num=num*num
                l+=1
            maxl=max(maxl,l)
            #print(i,visited,maxl)
            #print('------------------')
        return maxl if maxl>=2 else -1
        
```
```JAVA []
//This fails last two test cases but the same logic!!(90/92)
class Solution {
    public int longestSquareStreak(int[] nums) {
        Arrays.sort(nums);
        int maxlen=0,len=0;
        Set<Integer> visited=new HashSet<>();
        Set<Integer> checker=new HashSet<>();
        for(int i:nums){
            checker.add(i);
        }
        for(int n:nums){
            int num=n;
            len=1;
            while(checker.contains(num*num) && !visited.contains(num*num)){
                visited.add(num*num);
                num=num*num;
                len++;
            }
            maxlen=Math.max(maxlen,len);
        }
        return maxlen>=2?maxlen:-1;
    }
}
```

---

# Approach-2:HashMap+sort
# Intuition
- This is a clever way to solve a problem.
- We will `sort` as for the same reason stated above!
- The `map` stores the previosly found *perfect squares's streak*
- we will take square root of a current number `n` and store it in `sqroot` or `sqrt`.Magic happens here,if they are *perfect roots* and if they had any `prev` value in `map` which is `Dictionary or HashMap`,we increase the value(`val`) of stored `sqrt` and then map it from our current `num`.
- else then we create *map(key,val)* for it in `map`
```
nums=[1,4,16,2,256,3,5]
//after sort
nums=[1,2,3,4,5,16,256]
1->{1:1}
2->{1:1,2:1} //sqrt(2)=1.414
3->{1:1,2:1,3:1}
4->{1:1,2:1,3:1,4:2} //sqrt(4)=2[2:1]....Hence maintains STREAK!!
5->{1:1,2:1,3:1,4:2,5:1}
16->{1:1,2:1,3:1,4:2,5:1,16:3} //sqrt(16)=4[4:2]....STREAK!!
256->{1:1,2:1,3:1,4:2,5:1,16:3,256:4} //sqrt(256)=16[16:3]..STREAK!!
```
- This is optimised than previous code becuase `two loops are avoided!.`



# Complexity
- Time complexity:$O(N*log(N))$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:$O(N)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        maxlen=0
        map=dict()
        for n in nums:
            sqroot=int(math.sqrt(n))
            if sqroot*sqroot==n and sqroot in map:
                map[n]=map[sqroot]+1
                maxlen=max(maxlen,map[n])
            else:
                map[n]=1
        return maxlen if maxlen>=2 else -1
        
```
```JAVA []
class Solution {
    public int longestSquareStreak(int[] nums) {
        Arrays.sort(nums);
        int maxlen=0,sqrt=0;
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int n:nums){
            sqrt=(int)Math.sqrt(n);
            if(sqrt*sqrt==n && map.containsKey(sqrt)){
                map.put(n,map.get(sqrt)+1);
                maxlen=Math.max(maxlen,map.get(n));
            }
            else{
                map.put(n,1);
            }
        }
        return maxlen>=2?maxlen:-1;
    }
}
```

---


# Approach-3:set(Beats100%)
# Intuition
- This is kinda similar to *approach-1* but here we never mind about `visited`,just  do the same logic and convert `nums` *list* into a `set(list)`
- with help of a `set` DS(Data Structure),u can have $O(1)$
lookup.

# Complexity
- Time complexity:$O(N)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:$O(N)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums=set(nums)
        maxlen=0
        for n in nums:
            num=n
            l=1
            while num*num in nums:
                l+=1
                num*=num
            maxlen=max(maxlen,l)
        return maxlen if maxlen>=2 else -1
        
```
```JAVA []
//This fails last two test cases but the same logic!!(90/92)
class Solution {
    public int longestSquareStreak(int[] nums) {
        Arrays.sort(nums);
        int maxlen=0,len=0,num;
        Set<Integer> numss=new HashSet<>();
        for(int i:nums){
            numss.add(i);
        }
        for(int n:nums){
            num=n;
            len=1;
            while(numss.contains(num*num)){
                num*=num;
                len++;
            }
            maxlen=Math.max(maxlen,len);
        }
        return maxlen>=2?maxlen:-1;
    }
}
```
[GithubCodes for same probelm with dry run!!](https://github.com/themysterysolver/LEET-AND-FUN/tree/main/2586-longest-square-streak-in-an-array)
