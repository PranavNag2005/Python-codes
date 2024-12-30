class Graph:
    def __init__(self):
        self.adj_list={}
    def add_edge(self,node1,node2):
        if node1 not in self.adj_list:
            self.adj_list[node1]=[]
        if node2 not in self.adj_list:
            self.adj_list[node2]=[]
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)


    def dfs(self,start,visited=None):
        if visited is None:
            visited=set()
        visited.add(start)
        dfsorder=[start]
        for neighbour in self.adj_list[start]:
            if neighbour not in visited:
                dfsorder+=self.dfs(neighbour,visited)
        return dfsorder
    def display(self):
        for node,neighbour in self.adj_list.items():
            print(f"{node} {','.join(map(str,neighbour))}")

g=Graph()
num_edges=int(input())
for _ in range(num_edges):
    node1=int(input("enter node1 "))
    node2=int(input("enter node2 "))
    g.add_edge(node1,node2)
g.display()
start=int(input("enter the start node "))
dfsresult=g.dfs(start)
print(dfsresult)