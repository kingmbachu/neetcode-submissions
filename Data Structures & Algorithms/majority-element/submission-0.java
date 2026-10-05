class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> elementFreq = new HashMap<>();

        int treshold = nums.length / 2;

        for (int element : nums){
            if (!elementFreq.containsKey(element)){
                elementFreq.put(element,1);}
                else{

                    elementFreq.put(element, elementFreq.get(element) + 1);

                }
                
                if (elementFreq.get(element)  > treshold ){
                    return element;
                }
            }
                return -1;
        }

    }
