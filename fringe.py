class Fringe:
    __head = None
    __tail = None
    
    def __init__(self):
        self.__head = None
        self.__tail = None
        
    def add(self, newNode):
        p = self.__head
        if (self.__head == None):              # se la lista è vuota ...
            self.__head = newNode              # inserisci l'elemento
            self.__tail = self.__head
            newNode.next = None

        elif (newNode.val > self.__tail.val):  # se il valore è maggiore dell'ultimo ...
            self.__tail.next = newNode         # fai una append
            self.__tail = newNode
            newNode.next = None
            
        elif (newNode.val < self.__head.val):   # se è minore del primo ...
            newNode.next = self.__head          # inserisci in testa
            self.__head = newNode
            
        else:
            while(p.next != None and (newNode.val > p.next.val)): # scandisci la lista 
                p = p.next                                        # fino al punto di inserimento
            newNode.next = p.next
            p.next = newNode  
                
    def estrazione(self):
        p = self.__head
        if p == None:
            return None
        self.__head = self.__head.next
        p.next = None
        return p
            
    def empty_fringe(self):
        if self.__head == None:
            return True
        else:
            return False
        
    def stampa(self):
        print('Head', end = ' ')
        p = self.__head
        while p!= None:
            print(p.node.state.name, '->', end=' ')
            p = p.next
        print('Tail')
        