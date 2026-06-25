#include <unordered_set>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> mySet;

        for (auto item : nums) {
            if (mySet.find(item) != mySet.end()) {
                return true;
            } else {
                mySet.insert(item);
            }
        }
        return false;
    }
};
