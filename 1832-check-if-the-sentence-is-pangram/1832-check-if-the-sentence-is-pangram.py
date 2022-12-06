class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        mapAlphaOccur={character:0 for character in string.ascii_lowercase}
        for char in sentence:
            mapAlphaOccur[char]=1
        return sum(mapAlphaOccur.values())==26