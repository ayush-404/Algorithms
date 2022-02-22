// https://leetcode.com/problems/excel-sheet-column-number/
#include<string>
class Solution {
public:
    int titleToNumber(string columnTitle) {
        long long int ans = 0;
        long long int level = 1;
        for(int i = columnTitle.length() - 1; i>=0; i--){
          ans += (columnTitle[i] - 'A' + 1 )*level;
          level *= 26;
        }
        return ans;
    }
};