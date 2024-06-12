class Node:
    
    def __init__(self, state, parent, f, partial_path): 
        self.state = state
        self.depth = 0
        self.children = []
        self.parent = parent
        self.heuristic = f
        self.partial_path = partial_path
        
        
    def addChild(self, childNode):
        """
        Questo metodo aggiunge un nodo sotto un altro nodo
        """
        self.children.append(childNode)
        childNode.parent = self
        childNode.depth = self.depth + 1
        
    
    def printPath(self):
        """
        Questo metodo stampa il percorso dallo stato iniziale allo stato soluzione
        """
        if self.parent != None:
            self.parent.printPath()
        print("-> ", self.state.name)