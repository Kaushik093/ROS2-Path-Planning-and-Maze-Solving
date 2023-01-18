import cv2

from bot_mapping import bot_mapper
from bot_planning import DFS



bot_mapper_ = bot_mapper()

# sys.setrecursionlimit(10**6)


DFS_ = DFS()


def main():

    tiny = cv2.imread("/home/kaushik/Cropped_Thinned_Maze.png", cv2.IMREAD_GRAYSCALE)
    
    # cv2.imshow("tiny",tiny)
    # cv2.waitKey(0)

    
    # cv2.namedWindow("tiny_maze", cv2.WINDOW_FREERATIO)
    # cv2.imshow("tiny_maze", tiny)

    # [Mappring] Applying the One Pass Algorithm to Convert Maze Image to Graph
    bot_mapper_.one_pass(tiny)

    print("** Graph Extracted **\n")
    # bot_mapper_.Graph.display_graph()
    print("\n** =============== **\n")
    # cv2.waitKey(0)
    
    
    start = bot_mapper_.Graph.start
    # print("Start : {}".format(start))
    
    end =  (260, 49)

    paths = DFS_.get_paths(bot_mapper_.Graph.graph, start, end)

    tiny_rgb = cv2.cvtColor(tiny, cv2.COLOR_GRAY2RGB)
    # # cv2.imshow("tiny_maze", tiny_rgb)
    

    for path in paths:
        cv2.circle(tiny_rgb,(path[1],path[0]), 2, (120,120,0), -1 )
        cv2.imshow("tiny_maze", tiny_rgb)
       
    cv2.waitKey(0)
   
    # # # # Displaying found paths
    # print("Paths from {} to end {} is : \n {}".format(start, end, paths))
 

if __name__ == '__main__':
    main()
