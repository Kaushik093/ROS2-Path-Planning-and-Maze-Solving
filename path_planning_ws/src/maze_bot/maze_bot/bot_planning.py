import cv2
import numpy as np
import sys


sys.setrecursionlimit(10**6)


class bot_path_planner():

    def __init__(self):
        self.DFS = DFS()

    def path_illustrator(self,paths,maze):

        maze_rgb = cv2.cvtColor(maze, cv2.COLOR_GRAY2RGB)

        for path in paths:
            cv2.circle(maze_rgb, (path[1],path[0]), 1, (0,0,255), 1)
            cv2.imshow("maze", maze_rgb)
        cv2.waitKey(0)


    def find_path_nd_display(self,graph,start,end,maze,method = "DFS"):

        if method == "DFS":
            paths=DFS.get_paths(graph, start, end)
            self.path_illustrator(paths,maze)
        
        # elif method == "DFS_shortest":
        #     paths_costs = DFS.get_paths_cost(graph, start, end)
        #     paths = paths_costs[0]
            
        #     costs = paths_costs[1]
        #     min_cost = min(costs)
        #     path_to_display = paths[costs.index(min_cost)]
        #     self.path_illustrator(path_to_display,maze)


class DFS():

    # A not so simple problem, 
    #    Lets try a recursive approach
    @staticmethod
    def get_paths(graph,start,end,path = []):
        
        # Update the path to where ever you have been to
        path = path + [start]
       
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


    @staticmethod
    def get_paths_cost(graph,start,end,path=[],cost=0,trav_cost=0):

        # Update the path and the cost to reaching that path
        path = path + [start]
        cost = cost + trav_cost

        # 2) Define the simplest case
        if (start == end):
            return [path],[cost]
        # Handle boundary case [start not part of graph]
        if start not in graph.keys():
            return [],0

        # List to store all possible paths from point A to B
        paths = []
        # List to store costs of each possible path to goal
        costs = []

        # Retrieve all connections for that one damn node you are looking it
        for node in graph[start].keys():

            # Checking if not already traversed and not a "case" key
            if ( (node not in path) and (node!="case") ):

                new_paths,new_costs = DFS.get_paths_cost(graph,node, end,path,cost,graph[start][node]['cost'])

                for p in new_paths:
                    paths.append(p)
                for c in new_costs:
                    costs.append(c)
        
        return paths,costs


    

    


        