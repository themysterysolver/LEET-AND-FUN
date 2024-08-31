import java.util.ArrayList;
class Solution {
    public void print(int[] nums){
        for(int i:nums){
        System.out.print(i+" ");
       }
        System.out.println();
    }
    public void printAl(ArrayList<Integer> nums){
        for(int i:nums){
        System.out.print(i+" ");
       }
        System.out.println();
    }
    
    public void convert(int num[],ArrayList<Integer> n){
        for(int i:num){
            n.add(i);
        }
    }
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        print(nums1);
        print(nums2);
        ArrayList<Integer> n1=new ArrayList<>();
        ArrayList<Integer> n2=new ArrayList<>();
        convert(nums1,n1);
        convert(nums2,n2);
        printAl(n1);
        printAl(n2);
        int k=0;
        int[] num=new int[n1.size()];
        for(int p=0;p<n1.size();p++){
            num[p]=-1;
        }
        for(int i:n1){
            int index=n2.indexOf(i);
            for(int j=index;j<n2.size();j++){
                if (n2.get(j)>i){
                    num[k]=n2.get(j);
                    break;
                }   
            }
            k++;
        }
        return num;
    }
}