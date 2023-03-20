import os
from glob import glob
from setuptools import setup

package_name = 'AutoFollowCar'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name),
         glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='be105',
    maintainer_email='bensonw830@gmail.com',
    description='Beginner client libraries tutorials practice package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'drive = AutoFollowCar.drive:main',
            'get_jetson_info = AutoFollowCar.get_jetson_info:main',
            'operation = AutoFollowCar.operation:main',
            'test = AutoFollowCar.test:main',
            'talker = py_pubsub.publisher_member_function:main',
            'listener = py_pubsub.subscriber_member_function:main',
        ],
    },
)
