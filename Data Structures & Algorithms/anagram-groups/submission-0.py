class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {"".join(sorted(strs[0])): [strs[0]]}
        for i in range(1, len(strs)):
            sor_word = "".join(sorted(strs[i]))
            if sor_word in groups:
                groups[sor_word].append(strs[i])
            else:
                groups[sor_word] = [strs[i]]
        return list(groups.values())

