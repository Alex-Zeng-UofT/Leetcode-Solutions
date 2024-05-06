#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {

        int n = nums.size();
        int prefix[n];
        int postfix[n];
        std::vector<int> ret;

        prefix[0] = nums[0];
        postfix[n - 1] = nums[n - 1];

        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] * nums[i];
            postfix[n - 1 - i] = postfix[n - i] * nums[n - 1 - i];
        }

        for (int i = 0; i < n; i++) {

            if (i == 0 && i + 1 < n) 
                ret.push_back(postfix[i + 1]);

            else if (i == n - 1 && i - 1 >= 0)
                ret.push_back(prefix[i - 1]);

            else ret.push_back(prefix[i - 1] * postfix[i + 1]);
        
        }

        return ret;
    }
};