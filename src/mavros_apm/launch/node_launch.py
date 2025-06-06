# mavros_launch.py

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Declare launch arguments
    return LaunchDescription([
        DeclareLaunchArgument('fcu_url'),
        DeclareLaunchArgument('gcs_url'),
        DeclareLaunchArgument('tgt_system'),
        DeclareLaunchArgument('tgt_component'),
        DeclareLaunchArgument('pluginlists_yaml'),
        DeclareLaunchArgument('config_yaml'),
        DeclareLaunchArgument('log_output', default_value='screen'),
        DeclareLaunchArgument('fcu_protocol', default_value='v2.0'),
        DeclareLaunchArgument('namespace', default_value='mavros'),
        DeclareLaunchArgument('respawn_mavros', default_value='false'),

        Node(
            package='mavros',
            executable='mavros_node',
            namespace=LaunchConfiguration('namespace'),
            output=LaunchConfiguration('log_output'),
            parameters=[
                {'fcu_url': LaunchConfiguration('fcu_url')},
                {'gcs_url': LaunchConfiguration('gcs_url')},
                {'tgt_system': LaunchConfiguration('tgt_system')},
                {'tgt_component': LaunchConfiguration('tgt_component')},
                {'fcu_protocol': LaunchConfiguration('fcu_protocol')},
                LaunchConfiguration('pluginlists_yaml'),
                LaunchConfiguration('config_yaml'),
            ],
            respawn=LaunchConfiguration('respawn_mavros') == 'true'
        )
    ])

