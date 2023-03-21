import launch
from launch_ros.actions import ComposableNodeContainer
from launch.actions import ExecuteProcess
from launch_ros.descriptions import ComposableNode
from ament_index_python.packages import get_package_share_directory

# detect all 36h11 tags
cfg_36h11 = {
    "image_transport": "raw",
    "family": "36h11",
    "size": 0.162,
    "max_hamming": 0,
    "z_up": True
}

def generate_launch_description():
    # 'usb_cam' node from https://github.com/ros-drivers/usb_cam.git
    
    tag_node = ComposableNode(
        name='apriltag_36h11',
        namespace='apriltag',
        package='apriltag_ros', plugin='AprilTagNode',
        remappings=[
            # This maps the 'raw' images for simplicity of demonstration.
            # In practice, this will have to be the rectified 'rect' images.
            ("/apriltag/image_rect", "/camera/color/image_raw"),
            ("/apriltag/camera_info", "/camera/color/camera_info"),
        ],
        parameters=[cfg_36h11],
        extra_arguments=[{'use_intra_process_comms': True}],
    )
    container = ComposableNodeContainer(
        name='tag_container',
        namespace='apriltag',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[tag_node],
        output='screen'
    )
	
    bagplay = ExecuteProcess(cmd=['ros2', 'bag', 'play', get_package_share_directory('nxp_1')+"/data/rosbag2_2022_10_17-10_44_38/", "--loop"], shell=True)
    
    return launch.LaunchDescription([container, bagplay])
    
  
