# Topic

## Publisher
First we have to create a new node or if any exisiting node is there you can use that
You can check how you can create a node by referring to "Node_program.md"
Once you create a Node then you have to add a publisher in it 
For publisher two things are main i.Topic Name ii.Interface
Once you have the INterface that you want then go to the Node and make changes accordingly
```
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64 #importing the interface making that example_interfaces/msg/Int64
class NumberPublisherNode(Node): 
    def __init__(self):
        super().__init__('number_publisher')
        self.number_ = 2
        self.number_publisher_ = self.create_publisher(Int64, "temperature", 10) #to create a Publisher we need to use this syntax here we will mention the Topic name
        self.number_timer_ = self.create_timer(1.0, self.publish_number) #Publishing with timer from here
        self.get_logger().info('Number Publisher has been started.')
    def publish_number(self):
        msg = Int64()
        msg.data = self.number_
        self.number_publisher_.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode() 
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()
```

After done with the code in the node you have to build the package and also we are using different dependencies so we need to add that change in the package.xml <depend>exampe_interfaces</depend>

And for the execution of publisher we have to add <executable_name> = <package_name>.<node_name>:<function_name> in the setup.py file 

and then build package source workspace and run the publisher.

## Subscriber
