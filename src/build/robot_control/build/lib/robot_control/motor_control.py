import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16MultiArray

import Control_V3


class MotorSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Int16MultiArray,
            'motor_command',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # number of data received
        self.i = 1
        # speed and orientation motor left, speed and orientation motor right
        self.motor_left = 0
        self.motor_right = 0
        # robot object
        self.robot = Control_V3.RobotControl()

    def listener_callback(self):
        self.motor_left = msg.data[0]
        self.motor_right = msg.data[1]
        self.get_logger().info('Data received n°:"%s"', self.i)
        self.i +=1


def main():
    # init ros node
    rclpy.init(args=args)
    motor_sub = MotorSubscriber()

    # robot connection
    motor_sub.robot.connection()

    # init command
    motor_sub.robot.set_left_speed(0)
    motor_sub.robot.set_right_speed(0)

    while rclpy.ok():
        # receiving data
        rclpy.spin_once(motor_sub)

        # change motor command
        motor_sub.robot.set_left_speed(motor_sub.motor_left)
        motor_sub.robot.set_right_speed(motor_sub.motor_right)

        # sending motor command
        motor_sub.robot.sending_data()


if __name__ == '__main__':
    main()
