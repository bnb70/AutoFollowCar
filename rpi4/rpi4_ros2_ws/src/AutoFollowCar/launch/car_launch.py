from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='AutoFollowCar',
            namespace='Car',
            executable='get_jetson_info',
            name='jetson'
        ),
        Node(
            package='AutoFollowCar',
            namespace='Car',
            executable='operation',
            name='operation'
        ),
        Node(
            package='AutoFollowCar',
            namespace='Car',
            executable='drive',
            name='drive'
        ),

    ])