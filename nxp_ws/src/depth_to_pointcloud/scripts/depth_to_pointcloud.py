#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, PointCloud2
from cv_bridge import CvBridge
import numpy as np
import open3d as o3d

class DepthToPointCloud(Node):
    def __init__(self):
        super().__init__('depth_to_pointcloud')
        self.bridge = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            '/camera/depth/image_rect_raw',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.publisher = self.create_publisher(PointCloud2, '/pointcloud', 10)

    def listener_callback(self, msg):
        # Convert the ROS Image message to a NumPy array
        depth_image = self.bridge.imgmsg_to_cv2(msg)

        # Convert the depth image to a point cloud
        intrinsic_matrix = np.array([[611.055, 0, 319.5],
                                     [0, 611.055, 239.5],
                                     [0, 0, 1]])
        depth_scale = 0.0010000000474974513
        point_cloud = o3d.geometry.PointCloud.create_from_depth_image(
            depth_image, intrinsic_matrix, depth_scale)

        # Publish the point cloud
        point_cloud_msg = o3d.io.to_legacy_pointcloud_format(point_cloud)
        self.publisher.publish(point_cloud_msg)

def main(args=None):
    rclpy.init(args=args)
    depth_to_pointcloud = DepthToPointCloud()
    rclpy.spin(depth_to_pointcloud)
    depth_to_pointcloud.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
