#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {

        priority_queue<int> pq;

        for (int i : nums) pq.push(i);

        int ret = 0;
        for (int i = 0; i < k; i++, pq.pop()) {
            ret = pq.top();
        }

        return ret;
    }
};