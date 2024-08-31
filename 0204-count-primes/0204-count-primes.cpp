class Solution {
public:
     int countPrimes(int n) {
        if(n <= 2) 
            return 0;

        bool arr[n];
        arr[0] = arr[1] = false;
        int count = 0;
        for(int i=2; i<n; i++) {
            arr[i] = true; 
        }
        for(int i=2; i*i<n; i++) {
            if(arr[i]){
                for(int j=i<<1; j<n; j+=i)
                    arr[j] = false;
            }
        }
        for(int i=0;i<n;i++)
            if(arr[i])
                count++;

        return count;
     }
};