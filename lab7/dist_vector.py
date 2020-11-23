class Graph:

    def __init__(self, n):
        self.matrix =[]
        self.n=n     

    
    def add_edge(self, s, d, w):
        self.matrix.append((s, d, w))

    def print_path(self, dist,src):
        print("Vector Table of {}".format(chr(ord('A')+src)))
        print("Dest\tCost")
        for i in range(self.n):
            print("{0}\t{1}".format(chr(ord('A')+i), dist[i]))
            
    def algo(self, src):

        dist = [99] * self.n
        dist[src] = 0

        for _ in range(self.n - 1):
            for s, d, w in self.matrix:
                if dist[s] != 99 and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        self.print_path(dist,src)
        
if __name__ == "__main__":
    matrix=[]
    n=int(input("Enter No. of Routers : "))
    print("Enter the Adjacency Matrix :")
    for i in range(n):
        row=list(map(int,input().split(" ")))
        matrix.append(row)
    g=Graph(n)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==1 :
                g.add_edge(i,j,matrix[i][j])
    
    for i in range(n):
        g.algo(i)
