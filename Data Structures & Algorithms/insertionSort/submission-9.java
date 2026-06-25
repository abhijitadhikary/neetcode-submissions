// Definition for a pair
// class Pair {
//     int key;
//     String value;
//
//     Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {

        List<List<Pair>> returnList = new ArrayList<List<Pair>>();
        Pair temp;

        if (pairs.size() == 0) {
            return returnList;
        }        
        for (int index_pivot = 1; index_pivot < pairs.size(); ++index_pivot) {
            
            returnList.add(new ArrayList<Pair>(pairs));

            for (int index_left = 0; index_left < index_pivot; ++index_left) {
                if (pairs.get(index_pivot).key < pairs.get(index_left).key) {
                    temp = pairs.get(index_pivot);

                    for (int index_shift = index_pivot; index_shift > index_left; --index_shift) {
                        pairs.set(index_shift, pairs.get(index_shift - 1));
                    }
                    pairs.set(index_left, temp);
                }
            }
        }
        
        returnList.add(new ArrayList<Pair>(pairs));
        return returnList;
    }
}
