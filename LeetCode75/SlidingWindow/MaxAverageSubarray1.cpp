#include <vector>
using namespace std;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        
        double avg = 0;

        for (int i = 0; i < k; i++) avg += nums[i];

        double max = avg;

        for (int i = 1; i < nums.size() - k + 1; i++) {
            avg += (nums[i + k - 1] - nums[i-1]);

            if (avg > max) max = avg;
        }

        return max/k;
    }
};