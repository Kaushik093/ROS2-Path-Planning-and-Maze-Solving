import cv2
import numpy as np


''' DFS METHOD :
1. Start from entry 
2.Keep visiting nodes until dead end is found & backtrack after it is found to unvisited node
'''

class DFS():

           
        

    @staticmethod
    def get_paths(graph,start,goal,path=[]):
        path = path + [start]

        paths = []
        
        if(start == goal):
            return paths
        
        for node in graph[start].keys():
            if node not in path:
                new_paths=DFS.get_paths(graph,node,goal,paths)
                for p in new_paths:
                    paths.append(p)


        return paths



