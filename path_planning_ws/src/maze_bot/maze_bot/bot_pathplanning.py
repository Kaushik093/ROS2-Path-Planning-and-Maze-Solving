import cv2
import numpy as np
import sys

''' DFS METHOD :
1. Start from entry 
2.Keep visiting nodes until dead end is found & backtrack after it is found to unvisited node
'''

sys.setrecursionlimit(10**3)


class DFS():


    @staticmethod

    
    def get_paths(graph,start,goal,path=[]):
        path = path + [start]

        
        if(start == goal):
            return [path]
        
        if start not in graph.keys():
            return []        

        paths = []
        
        for node in graph[start].keys():
            if node not in path and node !="case":
                new_paths=DFS.get_paths(graph,node,goal,paths)
                for p in new_paths:
                    paths.append(p)


        return paths



