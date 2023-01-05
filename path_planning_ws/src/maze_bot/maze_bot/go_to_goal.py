import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist,Point
import math
import sys
from math import atan2,sqrt
import time

class robot_go_to_goal(Node):

    def __init__(self):
        super().__init__('goal_publisher')
        self.vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.pose_sub=self.create_subscription(Odometry,'/odom',self.pose_callback ,10)

        timer_period = 0.5  # How often go_to_goal function is called

        self.timer = self.create_timer(timer_period, self.go_to_goal_func)
        self.robot_pose=Point()
        self.goal_pose=Point()
        self.angle_to_goal=0.0
        self.distance_to_goal=0.0
        self.vel_msg=Twist()

    def pose_callback(self,data):        # Called when data is received by the subscriber     
        
        self.robot_pose.x=data.pose.pose.position.x
        self.robot_pose.y=data.pose.pose.position.y
        
        Quaternion=data.pose.pose.orientation
        
        (roll, pitch, yaw) = self.euler_from_quaternion(Quaternion.x,Quaternion.y,Quaternion.z,Quaternion.w)
        self.robot_pose.z=yaw
      

    def go_to_goal_func(self):

        self.goal_pose.x= float(sys.argv[1])
        self.goal_pose.y= float(sys.argv[2])
        self.angle_offset= float(sys.argv[3])

        vel_msg=Twist()


        self.distance_to_goal = math.sqrt(pow((self.goal_pose.x-self.robot_pose.x),2)+pow((self.goal_pose.y-self.robot_pose.y),2))
        
        self.angle_to_goal = math.atan2(self.goal_pose.y-self.robot_pose.y,self.goal_pose.x-self.robot_pose.x) 

        self.angle_to_goal = self.angle_to_goal + self.angle_offset
        self.angle_to_turn= (self.angle_to_goal - self.robot_pose.z ) 
        
        if abs(self.angle_to_turn)> 0.1 :
             
            self.get_logger().info('Turning')
            vel_msg.angular.z=self.angle_to_turn*0.35
            vel_msg.linear.x=0.0
        
        else:
             
            vel_msg.linear.x=self.distance_to_goal*0.35
            self.get_logger().info('Moving')
            
        if(self.distance_to_goal<0.1 ):
            vel_msg.linear.x=0.0
            vel_msg.angular.z=0.0
            self.get_logger().info('Goal Reached')
        
            

        msg = 'DTG: {:3f} ATG: {:3f} ATT: {:3f} Bot: {:3f}'.format(self.distance_to_goal, self.angle_to_goal * 180 / math.pi , self.angle_to_turn * 180 / math.pi, self.robot_pose.z * 180 / math.pi)
        self.get_logger().info(msg)
        
        self.vel_pub.publish(vel_msg)
    

    def euler_from_quaternion(self, x, y, z, w):
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
        return roll_x, pitch_y, yaw_z


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher =robot_go_to_goal()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()