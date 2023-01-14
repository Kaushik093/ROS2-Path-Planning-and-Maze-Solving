import cv2

from bot_mapping import bot_mapper


bot_mapper_ = bot_mapper()


def main():
    
    tiny = cv2.imread("/home/kaushik/Documents/ROS2-Path-Planning-and-Maze-Solving/path_planning_ws/src/maze_bot/maze_bot/test_maze.jpg",cv2.IMREAD_GRAYSCALE)
    # cv2.imshow("tiny",tiny)
    # cv2.waitKey(0)


    # Displaying Tiny Maze
    cv2.namedWindow("tiny_maze",cv2.WINDOW_FREERATIO)
    cv2.imshow("tiny_maze",tiny)    
    

    # [Mappring] Applying the One Pass Algorithm to Convert Maze Image to Graph
    bot_mapper_.one_pass(tiny)
    cv2.waitKey(0)

    


if __name__ == '__main__':
    main()