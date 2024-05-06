#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {

        int threshold = s.size();
        int i = 0;

        for (char c : t) {
            if (s[i] == c) i++;
            if (i == threshold) return true;
        }

        return s == t;
    }
};