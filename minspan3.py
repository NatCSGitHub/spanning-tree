import sys
import time
def prim(wc_graph):
  
    MST_list = []       
    visited_list = []   
    edge_list = []      

    min_edge = [0, 1, wc_graph[0][1]] 

    v = 0
    for V in range(vert_cout-1):
    
        visited_list.append(v)
    
        for u in range(vert_cout):
            if wc_graph[v][u] != 0:
                edge_list.append([v, u, wc_graph[v][u]])
        
        for e in range(1, len(edge_list)):
            if edge_list[e][2] < min_edge[2] and edge_list[e][1] not in visited_list:
                min_edge = edge_list[e]

        MST_list.append(min_edge)
      
        v = min_edge[1] 

        edge_list.remove(min_edge)
        min_edge = edge_list[0]

    return MST_list



file_name = 'city-pairs.txt'

vert_set = set()
with open(file_name) as f:
   for i in f:
       column = i.strip().split(' ')
       vert_set.add(column[0])
       vert_set.add(column[1])
f.close()

vert_list = list(vert_set)    
vert_cout = (len(vert_set))   

wc_graph = [[0 for i in range(vert_cout)] for j in range(vert_cout)]

with open(file_name) as f:
   for i in f:
       column = i.strip().split(' ')
       wc_graph[int(vert_list.index(column[0]))][int(vert_list.index(column[1]))]=int(column[2])
       wc_graph[int(vert_list.index(column[1]))][int(vert_list.index(column[0]))]=int(column[2])
f.close()

tic1 = time.perf_counter()
MST_list =  prim(wc_graph)
toc1 = time.perf_counter()

total = 0
print("Welcome to Oregon! \n PRIM'S ALGORITHM")
for i in range(len(MST_list)):
    print(vert_list[MST_list[i][0]], " to ", vert_list[MST_list[i][1]], " = ", MST_list[i][2], "miles")
    total += MST_list[i][2]
print("total weight: ", total, " miles.")
print(f"Time Prim's algorithm took: {1000*(toc1-tic1):0.4f} seconds") 
