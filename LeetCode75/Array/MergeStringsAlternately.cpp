#include <iostream>
#include <string>
#include <algorithm>

class Solution {
public:
    std::string mergeAlternately(std::string word1, std::string word2) {
        int len1 = word1.size();
        int len2 = word2.size();
        int longest = std::max(len1, len2);
        std::string builder = "";

        for (int i = 0; i < longest; i++) {
            if (i < len1) builder.push_back(word1[i]);
            if (i < len2) builder.push_back(word2[i]);
        }

        return builder;
    }
};