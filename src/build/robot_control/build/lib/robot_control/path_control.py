import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
import sensor_msgs.msg

from std_msgs.msg import Int64
from math import pi

class PathControl(Node):
    def __init__(self):
        super().__init__('path_controller')
        #lidar config
        scann = LaserScan()
        # from 0 to 360 range of data
        print("from 0 to 360 range of data: " + len(msg.ranges))
        # scan from 0 to 180
        scann.angle_min = -pi / 2
        scann.angle_max = pi / 2
        # increment each degree
        scann.angle_increment = pi/180
        # from 0 to 180 range of data
        print("from 0 to 180 range of data: " + len(msg.ranges))
        #range max of lidar : 40 meter
        scann.range_max = 40

        # publishing part
        # self.publisher_ = self.create_publisher(String, 'motor_command', 10)

        # subscribing part
        self.subscription = self.create_subscription(
            LaserScan,
            'laser_scan',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning


    def listener_callback(self, msg):
        self.get_logger().info('data [0] :' % msg.ranges[0])
        self.get_logger().info('data [90] :' % msg.ranges[90])
        self.get_logger().info('data [180] :' % msg.ranges[180])
        self.timer_callback()

def main(args=None):
    rclpy.init(args=args)
    path_controller = PathControl()

    rclpy.spin(path_controller)

    path_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


