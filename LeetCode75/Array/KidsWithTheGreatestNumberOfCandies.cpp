#include <vector>

class Solution {
public:
    std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies) {
        std::vector<bool> ret;
        int max = 0;

        for (int kid: candies) if (kid > max) max = kid;

        for (int kid: candies) ret.push_back(kid + extraCandies >= max);

        return ret;
    }
};