import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from scripts import GazeboRosPaths

def generate_launch_description():
    package_share_dir = get_package_share_directory("maze_bot")
    urdf_file = os.path.join(package_share_dir, "urdf", "maze_bot.urdf")

    model_path, plugin_path, media_path = GazeboRosPaths.get_paths()
    
    env = {
        "GAZEBO_MODEL_PATH": "/home/kaushik/Documents/ROS2-Path-Planning-and-Maze-Solving/path_planning_ws/install/maze_bot/share/maze_bot/..",
        "GAZEBO_PLUGIN_PATH": plugin_path,
        "GAZEBO_RESOURCE_PATH": media_path,
    }                         
    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=["gazebo","-s","libgazebo_ros_factory.so",],         # Terminal command to launch gazebo
                output="screen", 
                additional_env=env,
            ),
            Node(
                package="gazebo_ros",
                executable="spawn_entity.py",
                arguments=["-topic", "robot_description", "-entity", "robot", "-x", "0", "-y", "0", "-z", "0.0"],   # topic is the name of the ROS topic that contains the description of the entity to be spawned
                
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                output="screen",
                arguments=[urdf_file],
            ),
        ]
    )