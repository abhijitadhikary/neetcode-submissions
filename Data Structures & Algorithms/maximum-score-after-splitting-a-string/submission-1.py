class Solution:
    def maxScore(self, s: str) -> int:
        if len(s) < 2:
            return 0
        score_max = 0
        for idx in range(1,len(s)):
            score_max = max(score_max, s[:idx].count("0") + s[idx:].count("1"))
        return score_max

        