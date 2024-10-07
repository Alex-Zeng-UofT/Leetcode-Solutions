#include <vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {

        int most = 0;
        int left = 0, right = height.size() - 1;

        while (left < right) {

            int area = (right - left) * min(height[left], height[right]);
            
            if (area > most) most = area;

            if (height[left] < height[right])
                left++;
            else right--;

        }
        
        return most;
    }
};