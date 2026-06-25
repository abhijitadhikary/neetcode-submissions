class Solution:
    def maxScore(self, s: str) -> int:
        pf_0 = [0]
        pf_1 = [0]

        for idx in range(len(s)):
            c = s[idx]

            pf_0.append(pf_0[-1] + int(c == "0"))
            pf_1.append(pf_1[-1] + int(c == "1"))
        
        score_max = 0
        for idx in range(1,len(s)):
            score_max = max(score_max, pf_0[idx] + pf_1[-1] - pf_1[idx])
        return score_max