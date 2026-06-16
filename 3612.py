class Solution:
    def processStr(self, s: str) -> str:
        result = ""

        for ch in s:
            if ch.islower():
                result += ch
            elif ch == '*':
                if result:
                    result = result[:-1]
            elif ch == '#':
                result += result
            elif ch == '%':
                result = result[::-1]

        return result


# Testing di VS Code
if __name__ == "__main__":
    sol = Solution()

    s1 = "a#b%*"
    print(sol.processStr(s1))  # ba

    s2 = "z*#"
    print(sol.processStr(s2))  # ""

    # Tambahan test
    s3 = "abc#%"
    print(sol.processStr(s3))  # cbacba