import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist


class robot_go_to_goal(Node):

    def __init__(self):
        super().__init__('goal_publisher')
        self.vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.pose_sub=self.create_subscription(Odometry,'/odom',self.pose_callback ,10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.go_to_goal_func)
        

    def pose_callback(self,data):        # Called when data is received by the subscriber     
        
        robot_pose_x=data.pose.pose.position.x
        robot_pose_y=data.pose.pose.position.y
        robot_pose_z=data.pose.pose.position.z
        msg='X : {:3f} Y : {:3f} Z : {:3f}'.format(robot_pose_x,robot_pose_y,robot_pose_z)
        self.get_logger().info(msg)

    def go_to_goal_func(self):
        pass

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