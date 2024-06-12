from state import State
from node import Node
from elem import Elem
from fringe import Fringe
from euristics import h

def A_star():
            
        # crea la visited list
        close = []

        # crea la frontiera
        fringe = Fringe()
        
        # crea lo stato iniziale
        initialState = State()
        
        # crea la radice
        euristica = h[initialState.name]   
        root = Node(initialState, None, euristica, 0)         # il nodo padre della radice è None

        # aggiungi la radice alla fringe
        elemento = Elem(euristica, root)
        fringe.add(elemento)
        
        while not fringe.empty_fringe():                    # se la fringe non è vuota ...

            elem_estratto = fringe.estrazione()             # estrai l'elemento in testa
            currentNode = elem_estratto.node                # ottieni il nodo estratto
            currentState = currentNode.state
            print("-- dequeue --", currentState.name)
            
            if currentState.checkGoalState():           # se lo stato del nodo estratto è lo stato obiettivo ...
                print("Stato obiettivo raggiunto")          
                print("----------------------")
                print("Soluzione:")
                currentNode.printPath()                      # stampa il percorso trovato e termina l'elaborazione
                break     
                # verifica se lo stato del nodo estratto sta in close
            if currentState.name not in close:
                
                # aggiungiamo lo stato di questo nodo alla lista degli stati visitati
                close.append(currentState.name)
                
                # ottieni i nodi figli del nodo estratto dalla frontiera
                childStates = currentState.successorFunction()
            
                for (childStateName, distance) in childStates:
                    g = currentNode.partial_path + distance
                    euristica = h[childStateName]
                    f = g + euristica 
                    childNode = Node(State(childStateName), currentNode, f, g) 
                
                    # verifica se lo stato del nodo figlio sta in close
                    if childNode.state.name not in close:
                        # allora
                        # aggiungi il nodo figlio alla fringe
                        elemento = Elem(childNode.heuristic, childNode)
                        fringe.add(elemento) 

def main():            
    A_star()
    
main()