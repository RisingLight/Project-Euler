#include <iostream> 
#include <list> 
using namespace std; 
  
class Graph 
{ 
    int vertices;    
    list<int>* adjacent_lists;    
public: 
    Graph(int vertices)   { this->vertices = vertices; adjacent_lists = new list<int>[vertices]; } 
    ~Graph()       { delete [] adjacent_lists; } 
  
    void addEdge(int v, int w); 
    void greedyColoring(); 
}; 
  
void Graph::addEdge(int v, int w) 
{ 
    adjacent_lists[v].push_back(w); 
    adjacent_lists[w].push_back(v);   
} 
  
void Graph::greedyColoring() 
{ 
    int result[vertices]; 
    result[0]  = 0; 
  
    for (int u = 1; u < vertices; u++) {
        result[u] = -1; 
    }
  
    bool available[vertices]; 
    for (int color = 0; color < vertices; color++) {
        available[color] = false; 
    }
  
    for (int u = 1; u < vertices; u++) { 
        list<int>::iterator i; 
        for (i = adjacent_lists[u].begin(); i != adjacent_lists[u].end(); ++i) 
            if (result[*i] != -1) 
                available[result[*i]] = true; 
  
        int color; 
        for (color = 0; color < vertices; color++) {
            if (available[color] == false) 
                break; 
        }
  
        result[u] = color;
  
        for (i = adjacent_lists[u].begin(); i != adjacent_lists[u].end(); ++i) {
            if (result[*i] != -1) 
                available[result[*i]] = false; 
        }
    } 
  
    for (int u = 0; u < vertices; u++) 
        cout << "Vertex " << u << " --->  Color "
             << result[u] << endl; 
} 
  
int main() 
{ 
    Graph g1(5); 
    g1.addEdge(0, 1); 
    g1.addEdge(0, 2); 
    g1.addEdge(1, 2); 
    g1.addEdge(1, 3); 
    g1.addEdge(2, 3); 
    g1.addEdge(3, 4); 
    cout << "Coloring of graph 1 \n"; 
    g1.greedyColoring(); 
  
    Graph g2(5); 
    g2.addEdge(0, 1); 
    g2.addEdge(0, 2); 
    g2.addEdge(1, 2); 
    g2.addEdge(1, 4); 
    g2.addEdge(2, 4); 
    g2.addEdge(4, 3); 
    cout << "\nColoring of graph 2 \n"; 
    g2.greedyColoring(); 
  
    return 0; 
} 

