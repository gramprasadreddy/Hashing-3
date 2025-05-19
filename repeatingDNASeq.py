class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # T: O(1), S: O(n)
        seen = set()
        duplicates = set()

        for i in range(len(s) - 9):  # Iterate through all 10-letter substrings
            sub = s[i : i + 10]
            if sub in seen:
                duplicates.add(sub)  # Add repeated sequences
            seen.add(sub)

        return list(duplicates)