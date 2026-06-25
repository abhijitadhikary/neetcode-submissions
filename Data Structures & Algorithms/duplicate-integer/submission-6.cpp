class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if (nums.size() <= 1) return false;
        for (auto index_1=0; index_1<=nums.size()-2; index_1++) {
            for (auto index_2=index_1+1; index_2<=nums.size()-1; index_2++) {
                if (nums[index_1] == nums[index_2]) return true;
            }
        }
        return false;
    }
};
