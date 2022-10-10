import time
def sort_edges(wc_graph):

    sort_graph = []
    sort_graph.append(wc_graph[0])
    least = wc_graph[0]
    for i in range(1, len(wc_graph)):
        val = wc_graph[i][2]
        j = 0
        while val > sort_graph[j][2] and j < len(sort_graph) -1:
            j += 1
        sort_graph.insert(j , wc_graph[i])
        
    temp = sort_graph[len(sort_graph)-1]
    sort_graph.remove(sort_graph[len(sort_graph)-1])
    j = 0
    while temp[2] > sort_graph[j][2] and j < len(sort_graph) -1:
        j += 1
    sort_graph.insert(j , temp)

    return sort_graph


def find(root, parent):

    while root != parent[root]:
        root = parent[root]

    return root
    


def union(parent, rootv, rootu, size):
    
    if(size[rootv] > size[rootu]):
        parent[rootu] = rootv
        
    elif(size[rootv] < size[rootu]):
        parent[rootv] = rootu

    else:
        parent[rootu] = rootv
        size[rootv] += 1


def kurskal(wc_graph):

    MST_list = []
    
    sort_graph = sort_edges(wc_graph)

    parent = []
    size = []      

    for e in range(vert_cout):
        parent.append(e)
        size.append(0)

    encounter = 0
    k = 0       
    while encounter < (vert_cout - 1):
        v = sort_graph[k][0]
        u = sort_graph[k][1]
        k += 1
        rootu = find(v, parent)
        rootv = find(u, parent)
        if rootv != rootu:
            encounter = encounter +1
            MST_list.append([v, u, sort_graph[k][2]])
            union(parent, rootv, rootu, size)

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

wc_graph = []
with open(file_name) as f:
   for i in f:
        column = i.strip().split(' ')

        wc_graph.append([
            int(vert_list.index(column[0])),
            int(vert_list.index(column[1])),
            int(column[2])])
f.close()

tic = time.perf_counter()
MST_list = kurskal(wc_graph)
toc = time.perf_counter()

total = 0
print("Welcome to Oregon! \n KURSKAL'S ALGORITHM:")
for i in range(len(MST_list)):
    print(vert_list[MST_list[i][0]], " to ", vert_list[MST_list[i][1]], " = ", MST_list[i][2], "miles")
    total += MST_list[i][2]
print("total weight: ", total, " miles.")
print(f"Time Kurskal's algorithm took: {1000*(toc-tic):0.4f} seconds") 
