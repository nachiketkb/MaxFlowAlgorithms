from FordFulkerson import FlowNetwork

import time
fname = "graph3x3.txt"
for iterations in range (1,11):
    #fname = raw_input("Enter your file name:")
    maxnodes = iterations * 200
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
    start_time = time.time()
    g = FlowNetwork()    
    
    for i in range(1, maxnodes+1):#only add first 10*i nodes
        g.add_vertex(i)
        
    maxedges = 0
    for i in range(0,edges):
        line1 = f.readline()
        tmpArray =  line1.split()
        u = int(tmpArray[1])
        v = int(tmpArray[2])
        w = int(tmpArray[3])
        
        if(u <maxnodes+1 and v < maxnodes+1 and w > 0):
            
            #print u ,v, w
            g.add_edge(u,v,w)
            maxedges = maxedges + 1
            
    print "maxflow: " + str(g.max_flow(source, destination))
    print "maxnodes: " + str(maxnodes)
    print "maxedges: " + str(maxedges)
    print("--- %s seconds ---" % (time.time() - start_time))
    f.close()
    