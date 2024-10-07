#include <iostream>
#include <string>

class Solution {
public:
    // O(N) time, O(1) space
    std::string reverseWords(std::string s) {
        int i = 0;
        int last = 0;
        int len = s.size();

        // formatter
        while (i < len) {
            if (s[i] == ' ') {
                i++;
            } else {
                if (last != 0) s[last++] = ' '; 
                while (i < len && s[i] != ' ')
                    s[last++] = s[i++];
            }
        }
        // formatted string
        s = s.substr(0, last);

        // reverse string
        len = s.size();
        int left = 0;
        int right = len - 1;

        while (left <= right) {
            char temp = s[left];
            s[left++] = s[right];
            s[right--] = temp;
        }

        // reverse all words
        for (int j = 0; j < len; j++) {
            int count = 0;
            while (j < len && s[j] != ' ') {
                j++;
                count++;
            }

            int l = j - count;
            int r = j - 1;

            while (l <= r) {
                char temp = s[l];
                s[l++] = s[r];
                s[r--] = temp;
            }
        }

        return s;
    }
};