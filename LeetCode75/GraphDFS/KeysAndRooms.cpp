#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        
        queue<int> keys;
        bool visited[rooms.size()];

        for (int i = 0; i < rooms.size(); i++) visited[i] = false;

        keys.push(0);

        while (!keys.empty()) {
            int room = keys.front();
            keys.pop();

            if (visited[room]) continue;

            for (int i : rooms[room]) {
                keys.push(i);
            }

            visited[room] = true;
        }

        for (bool visit : visited) {
            if (!visit) return false;
        }

        return true;
    }
};