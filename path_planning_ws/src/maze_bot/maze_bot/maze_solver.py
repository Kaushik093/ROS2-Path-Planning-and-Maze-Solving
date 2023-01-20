import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import os
import numpy as np
from geometry_msgs.msg import Twist
from .bot_localization import bot_localizer
from .bot_mapping import bot_mapper
from .bot_planning import bot_path_planner

class VideoSaver(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscriber = self.create_subscription(Image,'/upper_camera/image_raw',self.get_video_feed_cb,10)   # Call get_video_feed_cb function when a frame is received
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.maze_solving)
        self.bot_localiser = bot_localizer()
        self.bot_mapper= bot_mapper()
        self.bot_path_planner = bot_path_planner()
        self.bridge = CvBridge()
        self.sat_view=np.zeros((100,130))
    
    def get_video_feed_cb(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg,'bgr8')
        self.sat_view = frame
        cv2.imshow('sat view',self.sat_view)
        cv2.waitKey(1)
    
    def maze_solving(self):
        frame_disp = self.sat_view.copy()
        self.bot_localiser.localise_bot(self.sat_view, frame_disp)
        self.bot_mapper.graphify(self.bot_localiser.maze_og)
        

        start = self.bot_mapper.Graph.start
        end = self.bot_mapper.Graph.end
        maze = self.bot_mapper.maze
         
        self.bot_path_planner.find_path_nd_display(self.bot_mapper.Graph,start,end,maze,method = "DFS")
        msg = Twist()
        msg.linear.x = 0.0
        # msg.angular.z = 0.5
        self.publisher_.publish(msg)
    
    

def main(args=None):
    rclpy.init(args=args)
    image_subscriber = VideoSaver()
    rclpy.spin(image_subscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
