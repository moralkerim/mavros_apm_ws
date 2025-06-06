# start_mavros_ardupilot.py

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():
    mavros_apm_share = get_package_share_directory('mavros_apm')

    return LaunchDescription([
        # Declare arguments
        DeclareLaunchArgument('fcu_url', default_value='udp://127.0.0.1:14550@14555'),
        DeclareLaunchArgument('gcs_url', default_value=''),
        DeclareLaunchArgument('tgt_system', default_value='1'),
        DeclareLaunchArgument('tgt_component', default_value='1'),
        DeclareLaunchArgument('log_output', default_value='screen'),
        DeclareLaunchArgument('fcu_protocol', default_value='v2.0'),
        DeclareLaunchArgument('respawn_mavros', default_value='false'),
        DeclareLaunchArgument('namespace', default_value='mavros'),

        # Include MAVROS node launch
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(mavros_apm_share, 'launch', 'node_launch.py')  # önceki dosya burada
            ),
            launch_arguments={
                'pluginlists_yaml': os.path.join(mavros_apm_share, 'config', 'apm_pluginlists.yaml'),
                'config_yaml': os.path.join(mavros_apm_share, 'config', 'apm_config.yaml'),
                'fcu_url': LaunchConfiguration('fcu_url'),
                'gcs_url': LaunchConfiguration('gcs_url'),
                'tgt_system': LaunchConfiguration('tgt_system'),
                'tgt_component': LaunchConfiguration('tgt_component'),
                'fcu_protocol': LaunchConfiguration('fcu_protocol'),
                'respawn_mavros': LaunchConfiguration('respawn_mavros'),
                'namespace': LaunchConfiguration('namespace'),
                'log_output': LaunchConfiguration('log_output'),
            }.items()
        )
#,
#                # Static transform: camera_link → base_link
#        Node(
#            package='tf2_ros',
#            executable='static_transform_publisher',
#            name='static_tf_camera_to_base',
#            arguments=['0', '0', '0', '0', '0', '0', 'camera_link', 'base_link']
#        ),
#
#        Node(
#            package='tf2_ros',
#            executable='static_transform_publisher',
#            name='static_tf_world_to_odom',
#            arguments=['0', '0', '0', '0', '0', '0', 'world', 'map']
#        ),
#
#        Node(
#            package='mavros_apm',
#            executable='odom_publisher',
#            name='odom_publisher',
#        ),

        #Node(
        #    package='topic_tools',
        #    executable='relay',
        #   name='odometry_relay',
        #   arguments=['/odometry', '/mavros/odometry/out'],
        #  remappings=[],
        #  output='screen'
        #),
    ])

