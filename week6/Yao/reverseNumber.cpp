/*
 * http://oj.leetcode.com/problems/reverse-integer/
 * Accepted
 * Date: April 19, 2014
 *
 */

class Solution {
    public:
        int reverse(int x) {
            int i, sign, val;
                    
            if((sign=x)<0)
            x = -x;
                
            val = 0;
            do{
                i = x % 10;
                val = 10*val + i;

            } while(x /= 10 );
            
            if(sign < 0)
                val = -val;
            return val;
        }
};
