import cv2

from bot_mapping import bot_mapper
from bot_planning import DFS


bot_mapper_ = bot_mapper()

# sys.setrecursionlimit(10**6)

DFS_ = DFS()


def main():

    tiny = cv2.imread("/home/kaushik/Cropped_Thinned_Maze.png", cv2.IMREAD_GRAYSCALE)
   
    # cv2.namedWindow("tiny_maze", cv2.WINDOW_FREERATIO)
    # cv2.imshow("tiny_maze", tiny)

    # [Mappring] Applying the One Pass Algorithm to Convert Maze Image to Graph
    bot_mapper_.one_pass(tiny)

    print("** Graph Extracted **\n")
    # bot_mapper_.Graph.display_graph()
    print("\n** =============== **\n")
    # cv2.waitKey(0)
    
    # print("Graph : {}".format(bot_mapper_.Graph.graph))
    
    start = bot_mapper_.Graph.start
    # print("Start : {}".format(start))
    
    end =(421, 0)

    paths = DFS_.get_paths(bot_mapper_.Graph.graph, start, end)
    paths_costs = DFS_.get_paths_cost(bot_mapper_.Graph.graph, start, end)
    # paths = paths_costs[0]
    
    # costs = paths_costs[1]
    # min_cost = min(costs)
    # path_to_display = paths[costs.index(min_cost)]
    # print("Shortest Path : {}".format(path_to_display))

    
    print("Paths from {} to end {} is : \n {}".format(start, end, paths))
    

    tiny_rgb = cv2.cvtColor(tiny, cv2.COLOR_GRAY2RGB)
    cv2.imshow("tiny_maze", tiny_rgb)
    

    for path in paths:
            cv2.circle(tiny_rgb, (path[1],path[0]), 1, (0,0,255), 1)
        
            cv2.imshow("tiny_maze", tiny_rgb)
       
    cv2.waitKey(0)
   
    # # # Displaying found paths
    
 

if __name__ == '__main__':
    main()
