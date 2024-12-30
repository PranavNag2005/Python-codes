class Directedgraph:
    def __init__(self):
        self.adjacent_list={}

    def add_vertex(self,vertex):
        if vertex not in self.adjacent_list:
            self.adjacent_list[vertex]=[]

    def add_edge(self,from_vertex,tovertex):
        if from_vertex not in self.adjacent_list:
            self.add_vertex(from_vertex)
        if tovertex not in self.adjacent_list:
            self.add_vertex(tovertex)
        self.adjacent_list[from_vertex].append(tovertex)


    def display(self):
        for vertex,edges in self.adjacent_list.items():
            print(f"{vertex} : {','.join(edges) if edges else 'None'}")

dg=Directedgraph()
dg.add_vertex('A')
dg.add_vertex('B')
dg.add_vertex('C')
dg.add_vertex('D')       
dg.add_edge("A","1")
dg.add_edge("B","10")
dg.add_edge("C","15")
dg.add_edge("D","20")


dg.display()