import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
    // creating the collection , in this case using hash maps    
        HashMap<Integer, Integer> indexOfMap = new HashMap<Integer,Integer>();
        for(int i = 0 ; i< nums.length ; i++){
            int reqNum = (target - nums[i]);
        if (indexOfMap.ContainsKey(reqNum)){
            int willReturn[] = {indexOfMap.get(reqNum) , i};
        }
            return willReturn;            
        }
        indexOfMap.put(nums[i], i);
    
    return null;


    }

    public static void main(String[] args) {

        Solution.target = 24;
        HashMap<Integer, Integer> indexx = new HashMap<Integer,Integer>();
        indexx.put(key =  0, Value = 7);
        indexx.put(key =  1, Value = 3);
        indexx.put(key =  2, Value = 1);
        indexx.put(key =  3, Value = 5);
        indexx.put(key =  4, Value = 2);
        indexx.put(key =  50, Value = 11);




        
    }}