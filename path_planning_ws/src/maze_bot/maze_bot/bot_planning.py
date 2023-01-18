import cv2
import numpy as np
import sys

sys.setrecursionlimit(10**6)


class DFS():

    # A not so simple problem, 
    #    Lets try a recursive approach
    @staticmethod
    def get_paths(graph,start,end,path = []):
        
        # Update the path to where ever you have been to
        path = path + [start]
        
        # print(path)

        # 2) Define the simplest case
        if (start == end):
            return path

        # Handle boundary case [start not part of graph]
        if start not in graph.keys():
            print("START NOT FOUND")
            return []
        # List to store all possible paths from start to end
        paths = []

        # 1) Breakdown the complex into simpler subproblems
        for node in graph[start].keys():
            
            if ( (node not in path) and (node!="case") ):
                # print(node)
                new_paths = DFS.get_paths(graph,node,end,path)
                for p in new_paths:
                    # print(paths)
                    paths.append(p)

        return paths
