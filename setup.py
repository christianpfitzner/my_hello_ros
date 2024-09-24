from setuptools import find_packages, setup

package_name = 'my_hello_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_hello_ros_publisher = my_hello_ros.my_hello_ros_publisher:main', 
            'my_hello_ros_subscriber = my_hello_ros.my_hello_ros_subscriber:main'
        ],
    },
)
