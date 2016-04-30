from FordFulkerson import FlowNetwork

import time
start_time = time.time()
fname = raw_input("Enter your file name:")
f = open(fname, 'r')

line1 = f.readline()
tmpArray =  line1.split()
nodes = int(tmpArray[2])
edges = int(tmpArray[3])

line1 = f.readline()
tmpArray =  line1.split()
source = int(tmpArray[1])
line1 = f.readline()
tmpArray =  line1.split()
destination = int(tmpArray[1])

print nodes, edges, source, destination

g = FlowNetwork()
for i in range(1, nodes+1):
    g.add_vertex(i)
    
count = 0
for i in range(0,edges):
    line1 = f.readline()
    tmpArray =  line1.split()
    u = int(tmpArray[1])
    v = int(tmpArray[2])
    w = int(tmpArray[3])
    count = count + 1
    if(w>0):
        #print u, v, w, count
        g.add_edge(u,v,w)
        
print (g.max_flow(source, destination))

print("--- %s seconds ---" % (time.time() - start_time))