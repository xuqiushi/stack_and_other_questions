class Solution:
    def _match_char(self, char, sub_p):
        if sub_p in {"*", "?"}:
            return True
        else:
            return sub_p == char

    def is_match(self, s: str, p: str) -> bool:
        if s == "":
            if p == "" or (len(set(list(p))) == 1 and list(set(list(p)))[0] == "*"):
                return True
            else:
                return False
        if p == "" and s != "":
            return False
        dp = [[False for _ in range(len(s))] for _ in range(len(p))]
        dp[0][0] = self._match_char(s[0] if s else "", p[0] if p else "")
        if p[0] == "*":
            for n in range(1, len(s)):
                dp[0][n] = True
        for m in range(1, len(p)):
            if p[m] == "*":
                dp[m][0] = dp[m - 1][0]
            else:
                dp[m][0] = (
                    self._match_char(s[0], p[m])
                    and len(set(list(p[:m]))) == 1
                    and list(set(list(p[:m])))[0] == "*"
                )
        for i in range(1, len(p)):
            for j in range(1, len(s)):
                if p[i] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i - 1][j - 1]
                else:
                    dp[i][j] = self._match_char(s[j], p[i]) and dp[i - 1][j - 1]
        return dp[len(p) - 1][len(s) - 1]


if __name__ == "__main__":
    test_s = "a"
    test_p = ""
    print(Solution().is_match(test_s, test_p))
