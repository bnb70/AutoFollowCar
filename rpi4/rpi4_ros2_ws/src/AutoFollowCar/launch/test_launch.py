from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='AutoFollowCar',
            namespace='Car',
            executable='talker',
            name='talker'
        ),
        Node(
            package='AutoFollowCar',
            namespace='Car',
            executable='listener',
            name='listener'
        ),

    ])