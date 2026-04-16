class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n1=nums.size();
        int n2=n1+1;//actual size
        int total_sum=(n2*(n2-1))/2;
        int sum=0;
        for(int i=0;i<n1;i++){
            sum=sum+nums[i];
        }
        return total_sum-sum;

        
    }
};