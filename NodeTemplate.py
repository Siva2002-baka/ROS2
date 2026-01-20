#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
class MyCustomNode(Node): #Modify Class Name
    def __init__(self):
        super().__init__('my_node_name') #Modify Node Name
def main(args=None):
    rclpy.init(args=args)
    node = MyCustomNode() #Modify Class Name
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()