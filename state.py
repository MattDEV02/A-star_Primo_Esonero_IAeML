from connections import connections

class State:
    def __init__(self, name = None):
        if name == None:
            self.name = self.getInitialState()   # crea stato iniziale
        else:
            self.name = name
            
    def getInitialState(state):
        initialState = 'Arad'
        return initialState
    
    def successorFunction(self):
        return connections[self.name]
    
    def checkGoalState(self):
        return self.name == 'Bucarest'