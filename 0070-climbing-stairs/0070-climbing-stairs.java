class Solution {
    public int climbStairs(int n) {
        if(n<=2)
            return n;
        else{
            ArrayList<Integer> num=new ArrayList<>();
            num.add(1);
            num.add(2);
            for(int i=2;i<n;i++){
                num.add(num.get(i-1)+num.get(i-2));
                System.out.println(num);
            }
            return num.get(num.size()-1);
        }
    }
}