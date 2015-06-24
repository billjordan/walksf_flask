import random
# import heapq
from queue import PriorityQueue
import timeit
from graph import SF_graph
import pickle
import node

class Dnode(object):
    """
    dnode is a wrapper for a node with a shortest path estimate that it can be sorted on
    """
    def __init__(self, node, d=float("inf"), pi=None):
        """
        d is the shortest path estimate
        pi is the nodes predecessor(dnode)
        """
        self.node = node
        self.d = d
        self.pi = pi
        
    def get_node(self):
        return self.node
    
    def get_d(self):
        return self.d
    
    def get_pi(self):
        return self.pi    
    
    def set_d(self, d):
        self.d = d
        
    def set_pi(self, pi):
        self.pi = pi
        
    def __lt__(self, other):
        return self.d < other.d
    
    def __str__(self):
        return "{} - d: {}".format(self.node.get_cnn(), self.d)
        

class Priority_queue(object):
    """
    min priority queue of SF_edges
    proritized by d
    where d is estimated shortest path 
    edges is a dict of edges
    """
    def __init__(self, nodes, start):
        """
        start node has a shortest path est of 0
        all other nodes have d = infinity
        all nodes have pi = None
        """
        self.queue = PriorityQueue()
        self.queue.put(Dnode(start, 0))
#         done = False
#         while not done:
#             try:
#                 node = nodes.pop()
#                 if node == start:
#                     self.queue.put(Dnode(node, 0))
#                 else:
#                     self.queue.put(Dnode(node))
#             except(KeyError):
#                 done = True
        
    def pop_dnode(self):
        return self.queue.get()
    
    def pop_node(self):
        return self.queue.get().get_node()
    
    def push_node(self, node, d):
        self.queue.put(Dnode(node, d))
        
    def push_dnode(self, dnode):
        self.queue.put(dnode)
        
    def empty(self):
        return self.queue.empty()
    
    
    
    
    
    
    
def randomInts(num=10):
    nums = list(range(num))
    randomNums = []
    for i in nums:
        randomNums.append(random.choice(nums))
    return randomNums
        
def printList(l):
    for i in l:
        print(i, "\t", end="")
        
def printSorted(l):
#     printList(l)

    queue = PriorityQueue()
    for i in l:
        queue.put(i)
    while not queue.empty():
#         print(queue.get(),  "\t", end="")
        queue.get()


if __name__ == '__main__':
    pass
#     gragh_pickle_in = open("sf_graph.pickle", "rb")
#     graph = pickle.load(gragh_pickle_in)
#     gragh_pickle_in.close()
#     print(graph.get_edges())
    
#     dic = {}
#     for i in (range(8)):
#         num = (10 ** i)
#         print(num)
#         l = randomInts(num)
#         dic[num] = (timeit.timeit("printSorted(l)", setup="from __main__ import printSorted, l", number=10))
#     
#     fout = open("results.csv", "w")
#     for key in sorted(dic.keys()):
#         fout.write("{},{}\n".format(key, dic[key]))
#         
#     fout.close()
#     l = randomInts(100)
#     print(timeit.timeit("printSorted(l)", setup="from __main__ import printSorted, l", number=100))