#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isVowel(char c) {
        return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
    }

    int maxVowels(string s, int k) {
        
        int count = 0;

        for (int i = 0; i < k; i++) 
            if (isVowel(s[i])) count++;

        int m = count;

        for (int i = k; i < s.size(); i++) {

            if (isVowel(s[i - k])) count--;
            if (isVowel(s[i])) count++;

            m = max(m, count);
        }

        return m;
    }
};