import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import os
from geometry_msgs.msg import Twist

class VideoSaver(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscriber = self.create_subscription(Image,'/upper_camera/image_raw',self.get_video_feed_cb,10)   # Call get_video_feed_cb function when a frame is received
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.maze_solving)
        
        self.bridge = CvBridge()
    
    def get_video_feed_cb(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg,'bgr8')
        cv2.imshow('output',frame)
        cv2.waitKey(1)
    
    def maze_solving(self):
        msg = Twist()
        msg.linear.x = 0.1
        # msg.angular.z = 0.5
        self.publisher_.publish(msg)
    
    

def main(args=None):
    rclpy.init(args=args)
    image_subscriber = VideoSaver()
    rclpy.spin(image_subscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
