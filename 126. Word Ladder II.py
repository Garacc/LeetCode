import collections
import string

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        bw:beginword
        ew:endword
        lw:linkword
        cw:currentword
        """
        def buildDict(wordList):
            dictionary = {}
            for w in wordList:
                for i in range(len(w)):
                    key = w[:i] + '_' + w[i + 1:]
                    dictionary[key] = dictionary.get(key, []) + [w]
            return dictionary
        
        def addLink(linklist, bw, ew, label_forw):
            if label_forw:
                linklist[bw] += [ew]
            else:
                linklist[ew] += [bw]
            return
        
        def Bfs(bw, ew, wordList, linklist, label_forw):
            if not bw: return False
            if len(bw) < len(ew):
                return Bfs(ew, bw, wordList, linklist, not label_forw)
            for w in (bw | ew):
                wordList.discard(w)
            lw, fin = set(), False
            while bw:
                cw = bw.pop()
                for add_letter in string.ascii_lowercase:
                    for i in range(len(cw)):
                        neighw = cw[:i] + add_letter + cw[i + 1:]
                        if neighw in ew:
                            fin = True
                            addLink(linklist, cw, neighw, label_forw)
                        if not fin:
                            lw.add(neighw)
                            addLink(linklist, cw, neighw, label_forw)
            return fin or Bfs(lw, ew, wordList, linklist, label_forw)
        
        def generatePath(bw, ew, linklist):
            if bw == ew:
                return [[bw]]
            else:
                return [[bw] + link for lw in linklist[bw] 
                        for link in generatePath(lw, ew, linklist)]

        linklist, paths = collections.defaultdict(list), []
        Bfs(bw = set([beginWord]), ew = set([endWord]), 
            wordList = set(wordList), linklist = linklist, label_forw = True)
        paths = generatePath(beginWord, endWord, linklist)
        
        return paths
        

'''
TOO SLOW!!!

from queue import Queue
import copy

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def buildDict(wordList):
            dictionary = {}
            for w in wordList:
                for i in range(len(w)):
                    key = w[:i] + '_' + w[i + 1:]
                    dictionary[key] = dictionary.get(key, []) + [w]
            return dictionary
        
        def Bfs(bw, ew, dictionary):
            queue = Queue()
            queue.put([bw, [bw], set([bw]), 1])
            minSteps = 100000
            while not queue.empty():
                cw, path, visited, steps = queue.get()
                if steps <= minSteps:
                    if cw == ew:
                        minSteps = steps
                        self.Ladders.append(path)
                        continue
                    
                    for i in range(len(cw)):
                        ckey = cw[:i] + '_' + cw[i + 1:]
                        neigh_ws = dictionary.get(ckey, [])
                        for neigh_w in neigh_ws:
                            if neigh_w not in visited:
                                cpath = copy.deepcopy(path)
                                cvisited = copy.deepcopy(visited)
                                cpath.append(neigh_w)
                                cvisited.add(neigh_w)
                                queue.put([neigh_w, cpath, cvisited, steps + 1])
            return 0
        
        self.Ladders = []
        dictionary = buildDict(wordList)
        Bfs(beginWord, endWord, dictionary)
        
        return self.Ladders
'''    
if __name__ == "__main__":  
    
    sol = Solution()
    bword = "qa"
    eword = "sq"
    wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    
    print(sol.findLadders(bword, eword, wordList))