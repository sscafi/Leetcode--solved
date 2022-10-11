class Solution {
    public String longestCommonPrefix(String[] strs) {
// this algorithim requires you to understand the Math class in java
        int size = strs.length;
        
// check if size is 0 return an empty string
        if ( size == 0){
            return "";
            
        } if ( size == 1){
            return strs[0];
        }
        
// sort the array
        Arrays.sort(strs);
        
// now find the minimum length from the first and last string
        int end = Math.min(strs[0].length(), strs[size -1].length());
        
// now find the common prefix between the first and last string
        int i = 0;
        while ( i < end && strs[0].charAt(i) == strs[size-1].charAt(i)){
            i++; 
            
        }
        String ski = strs[0].substring(0, i);
        return ski;
           
    }
}