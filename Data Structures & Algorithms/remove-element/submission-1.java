class Solution {
    public int removeElement(int[] nums, int val) {
     int k = nums.length;

     for (int i = 0; i < k; i++){
        if(nums[i] == val){
            int temp = nums[i];
            nums[i] = nums[--k];
            nums[k] = temp;

            i--;
        }
     }
      return k;   
    }
}