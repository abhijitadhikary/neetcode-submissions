class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        dict_anagrams = dict()
    
        for s in strs:
            char_count = [0]*26
            for c in s:
                char_count[ord(c)-ord("a")] += 1

            key_current = "".join(str(c) + "_" for c in char_count)
            dict_anagrams[key_current] = dict_anagrams.get(key_current, []) + [s]

        return [v for v in dict_anagrams.values()]



        # def is_anagram(a, b):
        #     if len(a) != len(b):
        #         return False

        #     dict_a = dict()
        #     for c in a:
        #         dict_a[c] = dict_a.get(c, 0) + 1
            
        #     for c in b:
        #         dict_a[c] = dict_a.get(c, 0) - 1
            
        #     return all(i==0 for i in dict_a.values())
            
        # dict_anagrams = dict()

        # for s in strs:
        #     s_sorted = "".join(sorted(s))

        #     if s_sorted not in dict_anagrams.keys():
        #         dict_anagrams[s_sorted] = [s]
        #     else:
        #         for s_candidate in dict_anagrams.keys():
        #             if is_anagram(s_sorted, s_candidate):
        #                 dict_anagrams[s_candidate].append(s)
                    
        # return [row for row in dict_anagrams.values()]
