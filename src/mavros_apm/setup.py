from setuptools import find_packages, setup
from glob import glob

package_name = 'mavros_apm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/node_launch.py']),
        ('share/' + package_name + '/launch', ['launch/apm_launch.py']),
        ('share/' + package_name + '/launch', ['launch/apm_launch_ser.py']),
        ('share/' + package_name + '/config', glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kerim',
    maintainer_email='moralkerim@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'odom_publisher = mavros_apm.odom_publisher:main'
        ],
    },
)
