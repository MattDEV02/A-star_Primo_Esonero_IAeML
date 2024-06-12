# connessioni tra città adiacenti con relative distanze

connections = {}

connections['Arad'] = [['Sibiu', 140], ['Timisoara', 118], ['Zerind', 75]]
connections['Bucarest'] = [['Fagaras', 211], ['Giurgiu', 90], ['Pitesti', 101], ['Urziceni', 85]]
connections['Craiova'] = [['Drobeta', 120], ['Pitesti', 138], ['Rimnicu Vilcea', 146]]
connections['Drobeta'] = [['Craiova', 120], ['Mehadia', 75]]
connections['Eforie'] = [['Hirsova', 86]]
connections['Fagaras'] = [['Bucarest', 211], ['Sibiu', 99]]
connections['Giurgiu'] = [[ 'Bucarest', 90]]
connections['Hirsova'] = [['Eforie', 86], ['Urziceni', 98]]
connections['Iasi'] = [['Neamt', 87], ['Vaslui', 92]]
connections['Lugoj'] = [[ 'Mehadia', 70], ['Timisoara', 111]]
connections['Mehadia'] = [['Drobeta', 75], ['Lugoj', 70]]
connections['Neamt '] = [['Iasi', 87]]
connections['Oradea'] = [['Sibiu', 151], ['Zerind', 71]]
connections['Pitesti'] = [['Bucarest', 101], ['Craiova', 138], ['Rimnicu Vilcea', 97]]
connections['Rimnicu Vilcea'] = [['Craiova', 146], ['Pitesti', 97], ['Sibiu' , 80]]
connections['Sibiu'] = [['Arad', 140], ['Fagaras', 99], ['Oradea', 151], ['Rimnicu Vilcea', 80]]
connections['Timisoara'] = [['Arad', 118], ['Lugoj', 111]]
connections['Urziceni'] = [['Bucarest', 85], ['Hirsova', 98], ['Vaslui', 142]]
connections['Vaslui'] = [['Iasi', 92], ['Urziceni', 142]]
connections['Zerind'] = [['Arad', 75], ['Oradea', 71]]