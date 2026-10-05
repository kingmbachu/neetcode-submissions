class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seenNums = new HashMap<>();
        

        for (int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            if (seenNums.containsKey(complement)){
                return new int[]{seenNums.get(complement), i};
            }
            seenNums.put(nums[i], i);
        }
        return new int[]{};
    }
}
