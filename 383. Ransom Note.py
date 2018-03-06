class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        if not ransomNote: return True
        
        notedict = {}
        for word in ransomNote:
            if notedict.get(word, 0):
                notedict[word] += 1
            else:
                notedict[word] = 1
        
        for word in magazine:
            if notedict.get(word, 0):
                notedict[word] = max(0, notedict[word] - 1)
            if not sum(notedict.values()):
                return True
        return False