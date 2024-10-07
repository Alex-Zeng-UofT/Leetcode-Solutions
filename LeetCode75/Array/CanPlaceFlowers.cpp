#include <iostream>
#include <vector>

class Solution {
public:
    bool canPlaceFlowers(std::vector<int>& flowerbed, int n) {
        int count = 0;
        int len = flowerbed.size();

        for (int i = 0; i < len; i++) {

            bool leftEmpty = (i == 0) || (flowerbed[i - 1] == 0);
            bool rightEmpty = (i == len - 1) || (flowerbed[i + 1] == 0);

            if (flowerbed[i] == 0 && leftEmpty && rightEmpty) {
                count++;
                flowerbed[i] = 1;
                i++;
            }

            if (count == n) return true;
        }

        return count >= n;
    }
};