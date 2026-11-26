class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def get_n_primes(n_primes):
            def is_prime(num):
                if num < 2:
                    return False
                    
                for current_candidate in range(2, num//2 + 1):
                    if num % current_candidate == 0:
                        return False
                return True

            prime_count = 0
            index = 0
            list_primes = []
            while prime_count < n_primes:
                if is_prime(index):
                    list_primes.append(index)
                    prime_count+=1
                index += 1
            return list_primes

        prime_list_26 = get_n_primes(26)
        alphabet_prime_map = {chr(ord("a") + i): prime_list_26[i] for i in range(26)}

        dict_anagrams = {}

        for s in strs:
            current_prime_key = 1
            for c in s:
                current_prime_key *= alphabet_prime_map[c]
            
            dict_anagrams[current_prime_key] = dict_anagrams.get(current_prime_key, []) + [s]
        
        return [v for v in dict_anagrams.values()]



        # dict_anagrams = dict()
    
        # for s in strs:
        #     char_count = [0]*26
        #     for c in s:
        #         char_count[ord(c)-ord("a")] += 1

        #     key_current = "".join(str(c) + "_" for c in char_count)
        #     dict_anagrams[key_current] = dict_anagrams.get(key_current, []) + [s]

        # return [v for v in dict_anagrams.values()]



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
