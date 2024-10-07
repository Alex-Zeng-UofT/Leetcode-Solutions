#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string removeStars(string s) {
        
        vector<char> stack;
        string ret = "";

        for (char c : s) {
            if (c == '*') {
                stack.pop_back();
            } else {
                stack.push_back(c);
            }
        }

        for (char c : stack) ret += c;

        return ret;
    }
};