// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    vector<vector<Pair>> insertionSort(vector<Pair>& pairs) {
        vector<vector<Pair>> returnList;
        std::size_t len = pairs.size();

        if (len == 0) {
            return returnList;
        }

        Pair tempPair(-1, "ERROR");

        for (std::size_t index_pivot = 1; index_pivot < len; ++index_pivot) {
            returnList.push_back(pairs);
            for (std::size_t index_left = 0; index_left < index_pivot; ++index_left) {
                if (pairs.at(index_pivot).key < pairs.at(index_left).key) {
                    tempPair = pairs.at(index_pivot);
                    for (std::size_t index_shift = index_pivot; index_shift > index_left; --index_shift) {
                        pairs.at(index_shift) = pairs.at(index_shift - 1);
                    }
                    pairs.at(index_left) = tempPair;
                    break;
                }
            }
        }
        returnList.push_back(pairs);
    }
};
