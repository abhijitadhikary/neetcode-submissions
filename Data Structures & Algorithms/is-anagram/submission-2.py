class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not (len(s) == len(t)):
            return False
        s = s.lower()
        t = t.lower()

        seen_list = []

        for index in range(len(s)):
            s_c = s[index]
            seen_list.append(s_c)

        for index in range(len(t)):
            t_c = t[index]
            try:
                seen_list.remove(t_c)
            except ValueError as e:
                break
        
        return len(seen_list) == 0

        