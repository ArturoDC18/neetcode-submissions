class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            word = sorted(string)
            comparable = "".join(word)
            if comparable in anagrams:
                anagrams[comparable].append(string)
            else:
                anagrams[comparable] = [string]
        lista = []
        for key in anagrams:
            lista.append(anagrams[key])
        return lista
