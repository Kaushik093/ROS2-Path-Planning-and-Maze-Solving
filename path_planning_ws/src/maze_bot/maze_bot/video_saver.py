import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import os

class VideoSaver(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscriber = self.create_subscription(Image,'/upper_camera/image_raw',self.process_data,10)   # Call process_data function when a frame is received
        vid_path = os.path.join(os.getcwd(),'video.avi')
        self.out = cv2.VideoWriter(vid_path,cv2.VideoWriter_fourcc('M','J','P','G'),30,(1280,720 ))
        self.bridge = CvBridge()
    
    def process_data(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg,'bgr8')
        self.out.write(frame)
        cv2.imshow('frame',frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    image_subscriber = VideoSaver()
    rclpy.spin(image_subscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
