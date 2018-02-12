class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        
        self.outputstr = ""
        
        def midorder(Node):
            if not Node: return
            
            self.outputstr += str(Node.val)
            if(Node.left != None and Node.right != None):
                self.outputstr += "("
                midorder(Node.left)
                self.outputstr += ")("
                midorder(Node.right)
                self.outputstr += ")"
            elif(Node.left == None and Node.right != None):
                self.outputstr += "()("
                midorder(Node.right)
                self.outputstr += ")"
            elif(Node.left != None and Node.right == None):
                self.outputstr += "("
                midorder(Node.left)
                self.outputstr += ")"
                
            return
        
        midorder(t)
        
        return self.outputstr