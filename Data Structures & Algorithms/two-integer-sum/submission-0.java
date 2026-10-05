class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> seenNum = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            if (seenNum.containsKey(complement)){
                return new int [] {seenNum.get(complement), i};
            }
            else {
                seenNum.put(nums[i], i);
            }
        }
        return new int[]{};
        
    }
}
