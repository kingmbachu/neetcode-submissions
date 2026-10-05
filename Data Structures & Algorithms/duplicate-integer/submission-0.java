class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> uniqueNums = new HashSet<>();

        for (int x: nums){
            if (uniqueNums.contains(x)){
                return true;
            }
            uniqueNums.add(x);
        }

        return false;

        
    }
}