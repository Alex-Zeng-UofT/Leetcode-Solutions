#include <iostream>
#include <vector>


class Solution {
public:
    int compress(std::vector<char>& chars) {
        int pointer = 0;
        
        for (int i = 0; i < chars.size(); i++) {
            int count = 0;
            int cur = chars[i];

            while (i < chars.size() && chars[i] == cur) {
                count++;
                i++;
            }

            chars[pointer++] = cur;
            
            if (count > 1)
                for (char c : std::to_string(count)) 
                    chars[pointer++] = c;
               
            i--;
        }
        
        return pointer;
    }
};