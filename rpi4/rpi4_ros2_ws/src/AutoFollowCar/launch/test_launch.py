from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='AutoFollowCar',
            namespace='talker',
            executable='talker',
            name='sim'
        ),
        Node(
            package='AutoFollowCar',
            namespace='listener',
            executable='listener',
            name='sim'
        ),

    ])