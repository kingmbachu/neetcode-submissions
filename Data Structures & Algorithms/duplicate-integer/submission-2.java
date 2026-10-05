class Solution {
    public boolean hasDuplicate(int[] nums) {
        int[] checkdup = new int[nums.length];
        int count = 0;
        for(int i = 0; i < nums.length; i++){
            for(int j = 0; j <count; j++){
                if(checkdup[j] == nums[i]){
                    return true;
                } 

            }
            checkdup[count++] = nums[i];
        }
        return false;
    }
}