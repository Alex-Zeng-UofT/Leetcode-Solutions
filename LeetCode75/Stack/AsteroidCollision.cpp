#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        
        vector<int> ret;

        for (int i : asteroids) {
            
            int n = ret.size() - 1;

            if (n < 0 || i > 0 || ret[n] < 0) ret.push_back(i);
            else {
                int j;
                for (j = n; j >= 0; j--) {
                    int top = ret[j];
                    if (top > 0 && top <= 0 - i) {
                        ret.pop_back();
                        if (top == 0 - i) break;
                    }
                    else break;
                }
                if (j < 0 || ret[j] < 0) ret.push_back(i);
            }
        }

        return ret;
    }
};