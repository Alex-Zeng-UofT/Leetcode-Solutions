#include <iostream>
#include <string>

class Solution {
public:

    bool isVowel(char c) {
        return (c == 'a' || c == 'A' || c == 'e' || c == 'E' 
                || c == 'i' || c == 'I' || c == 'o' || c == 'O'
                || c == 'u' || c == 'U');
    }

    std::string reverseVowels(std::string s) {

        int left = 0;
        int right = s.size() - 1;

        while (left < right) {

            while (left < right && !isVowel(s[left])) 
                left++;

            while (left < right && !isVowel(s[right])) 
                right--;
            
            char temp = s[left];
            s[left++] = s[right];
            s[right--] = temp;
        }

        return s;
    }
};