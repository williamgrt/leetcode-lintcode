// Source : https://leetcode.com/problems/powx-n/
// Author : henrytine
// Date   : 2020-07-25

/***************************************************************************************************** 
 *
 * Implement pow(x, n), which calculates x raised to the power n (xn).
 * 
 * Example 1:
 * 
 * Input: 2.00000, 10
 * Output: 1024.00000
 * 
 * Example 2:
 * 
 * Input: 2.10000, 3
 * Output: 9.26100
 * 
 * Example 3:
 * 
 * Input: 2.00000, -2
 * Output: 0.25000
 * Explanation: 2-2 = 1/22 = 1/4 = 0.25
 * 
 * Note:
 * 
 * 	-100.0 < x < 100.0
 * 	n is a 32-bit signed integer, within the range [&minus;231, 231 &minus; 1]
 * 
 ******************************************************************************************************/

class Solution {
public:
    double myPow(double x, int n) {
        long long N = n;
        if (N < 0) {
            N = (-N);
            x = 1 / x;
        }
        return fast_pow(x, N);
    }
    
    double fast_pow(double x, int n) {
        if (n == 0) return 1.0;
        double half = fast_pow(x, n / 2);
        if ( n % 2 == 0) {
            return half * half
        }
        else {
            return half * half * x;
        }
    }
};