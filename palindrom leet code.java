class Solution {
    public boolean isPalindrome(int x) {
        // base condition
        if ( x < 0) {
        return false;
        }
        // to store the number in a variable 
        int number = x;
        int y = 0;
        while ( number > 0){
               y = y * 10 + number % 10 ;
            number  = number / 10 ;
        }
        return x == y;
          
        
}
}