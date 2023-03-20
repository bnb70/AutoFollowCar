from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='AutoFollowCar',
            namespace='jetson',
            executable='get_jetson_info',
            name='sim'
        ),
        Node(
            package='AutoFollowCar',
            namespace='car_info',
            executable='drive',
            name='sim'
        ),
        Node(
            package='AutoFollowCar',
            namespace='operation',
            executable='operation',
            name='sim'
        ),

    ])