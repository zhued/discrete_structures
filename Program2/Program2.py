# Programming Assignment 2
# Edward Zhu

import itertools
import time
import math

#import the graph 17x17 size from the website we were linked
with open ('input.txt', 'r') as data:
	datagraph = [];
	for lines in data:
		numbers = lines.split()
		numbers = map(int, numbers)
		datagraph.append(numbers)
 #~ test data of 5x5 data 
testdata = ([0, 3, 7, 6, 8],
			[3, 0, 7, 4, 5],
			[7, 7, 0, 3, 9],
			[6, 4, 3, 0, 4],
			[8, 5, 9, 4, 0])
 #~ taking the path and finding the cost 
def getcost(path, graph):
	cost = 0
	prevnode = path[0]
	for node in path[1:]:
		if graph[prevnode][node] == 0:
			break
		cost += graph[prevnode][node]
		prevnode = node
	return cost

# edge class (part of cheapest link)
class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight
        self.taken = False
        self.discarded = False
#~ take the edge bc valid
    def take(self):
        self.taken = True
#~ untake edge
    def untake(self):
        self.taken = False
#~ discard edge because unvalid
    def discard(self):
        self.discarded = True
#~ undiscard
    def undiscard(self):
        self.discarded = False
#~ et other node across edge
    def getother(self, node):
        if node == self.second:
            return self.first
        else:
            return self.second

    def __repr__(self):
        return ("%s -- %d -- %s") % (self.first.name, self.weight, self.second.name)

# Node class (part of cheapest link)
class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []
#~ add an edge
    def addedge(self, edge):
        self.edges.append(edge)
#~ take an edge
    def taken_edges(self):
        return filter(lambda x: x.taken, self.edges)
#~ find next edge while walking
    def findnext(self, edge):
        edges = filter(lambda x: x != edge, self.taken_edges())
        if len(edges) == 0:
            return None
        else:
            return edges[0]

    def __str__(self):
        return self.name

# Graph class (part of cheapest link)
class Graph:
    def __init__(self, matrix):
        self.nodes = []
        self.edges = []
        for i, row in enumerate(matrix):
            self.nodes.append(Node(i))
        for node, edges in enumerate(matrix):
            for to, weight in enumerate(edges):
                if to > node and weight != 0:
                    e = Edge(self.nodes[node], self.nodes[to], weight)
                    self.nodes[node].addedge(e)
                    self.nodes[to].addedge(e)
                    self.edges.append(e)

    def clear(self):
        for edge in self.edges:
            edge.untake()
            edge.undiscard()
#~ check if path is valid
    def valid(self, edge):
        edge.take()
        for node in self.nodes:
            if len(node.taken_edges()) >= 3:
                edge.untake()
                return False
        start = edge.first
        next_edge = start.findnext(edge)
        if next_edge is None:
            edge.untake()
            return True
        node = start
        while next_edge is not None:
            node = next_edge.getother(node)
            if node == start:
                edge.untake()
                return False
            next_edge = node.findnext(next_edge)
        edge.untake()
        return True
#~ get next edge on opposite end of node
    def getnextedge(self):
        edges = filter(lambda x: not x.discarded and not x.taken, self.edges)
        if edges == []:
            return None
        nextedge = min(edges, key = lambda x: x.weight)
        while not self.valid(nextedge):
            nextedge.discard()
            edges = filter(lambda x: not x.discarded and not x.taken, self.edges)
            if edges == []:
                return None
            nextedge = min(edges, key = lambda x: x.weight)
        nextedge.take()
        return nextedge
#~ actual funcion to run cheapest link
    def cheapestlink(self):
        edges = []
        edge = self.getnextedge()
        while edge is not None:
            edges.append(edge)
            edge = self.getnextedge()

        endnodes = filter(lambda x: len(x.taken_edges()) == 1, self.nodes)
        last_edge = filter(lambda x: (x.first in endnodes and x.second in endnodes), self.edges)
        self.clear()
        return edges + last_edge
		
#exhaustive search
def ES(graph):
	#~ t1 = time.time()
	nodes = []
	mincost = 0
	for i in range(0, len(graph)):
		nodes.append(i)
	test = list(itertools.permutations(nodes))
	#~ subset = len(test)/100000
	for x in range(0, len(test)):
		current = test[x]
		if mincost == 0 or mincost > getcost(current, graph):
			mincost = getcost(test[x], graph)
			minpath = current
	#~ elapsed = time.time() - t1
	#~ return elapsed
	return minpath
	
print
print('EXHAUSTIVE SEARCH:')	
#~ Tried to implement the time functions, but it was failing after 5 seconds of running it
#~ Below is calculating average computations times conceptually
print('Years to Finish 17x17 dataset:')
k = math.factorial(17)
cps = 10000 #lets assume 10000 calculation of each path per second
sec = 60*60*24*365 #seconds in a year
print(k/(cps*sec))
print('Shortest Path for Test 5x5 dataset:')	
print(ES(testdata))
print('Path Cost:')	
print(getcost(ES(testdata), testdata))
print('Average Runtime from 10 runs(seconds):')	
total = 0
for x in range(0,10):
	t1 = time.time()
	ES(testdata)
	elapsed = time.time() - t1
	total += elapsed
avg = total/10
print avg

#nearest neighbor
def NN(graph, start):
	path = [start]
	node = start
	while len(path) < len(graph):
		row = graph[node]
		isvalid = filter(lambda x: x[0] not in path and x[0] != node and x[1] != 0, enumerate(row))
		if (isvalid == 0 ):
			break
		nextnode = min(isvalid, key = lambda x: x[1])[0]
		path.append(nextnode)
	path.append(start)
	return path
	
print
print('NEAREST NEIGHBOR:')
print('Shortest Path:')		
print(NN(datagraph,0))
print('Path Cost:')	
print(getcost(NN(datagraph,0), datagraph))
print('Average Runtime from 10 runs(seconds):')	
total = 0
for x in range(0,10):
	t1 = time.time()
	NN(datagraph,0)
	elapsed = time.time() - t1
	total += elapsed
avg = total/10
print avg
		
#repeated nearest neighbor
def RNN(graph):
	rnnlist = []
	mincost = 0
	for i in range(0, len(graph)):
		current = NN(datagraph, i)
		if mincost == 0 or mincost > getcost(current, graph):
			mincost = getcost(current, graph)
			minpath = current
	return minpath

print
print('REPEATED NEAREST NEIGHBOR:')
print('Shortest Path:')	
print(RNN(datagraph))
print('Path Cost:')	
print(getcost(RNN(datagraph), datagraph))
print('Average Runtime from 10 runs(seconds):')	
total = 0
for x in range(0,10):
	t1 = time.time()
	RNN(datagraph)
	elapsed = time.time() - t1
	total += elapsed
avg = total/10
print avg	

#cheapest link
structured = Graph(datagraph)
d = structured.cheapestlink()

print
print('CHEAPEST LINK:')
print('Shortest Path:')	
for x in d:
    print "(%s, %s)" % (x.first.name, x.second.name)
print('Path Cost:')	
print sum(map(lambda x: x.weight, d))
print('Average Runtime from 10 runs(seconds):')	
total = 0
for x in range(0,10):
	t1 = time.time()
	structured.cheapestlink()
	elapsed = time.time() - t1
	total += elapsed
avg = total/10
print avg
print

#~ Results:
#~ It seems like Cheapest Link returns the fastest path in the graph, but 
#~ also runs longer than repeated nearest neighbor. Nearest Neighbor doesn't 
#~ seem to be the most optimal purely because one would be randomly choosing 
#~ a node to start on, which will not always be the most efficient. Repeated
#~ Nearest Neighbor runs through every node as a starting node, thus it will 
#~ yield better results with more time to run it. And then comes exhaustive 
#~ search, which takes way too long, but it would give back the fastest way 
#~ to traverse the graph, however it is way too long to wait because it is 
#~ factorial time. Excluding Exhaustive Search, Cheapest Link took the longest 
#~ to run, then Repeated Nearest Neighbor, and then Nearest Neighbor. But 
#~ it can be seen that the more time an algorithm takes to run, the better 
#~ the results will be. Cheapest Link came out with a cost of 2189, which 
#~ is very very close to the actual value of 2085.

