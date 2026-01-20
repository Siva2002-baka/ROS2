# ROS2 Program

## Creating a Package
```
cd ~/ros2_ws/src/
ros2 pkg <package_name> --build-type ament_python --dependencies rclpy
```

## Creating a Node
```
cd ~/ros2_ws/src/packagename/packagename/
touch <Node_Name.py>
chmod +x <Node_Name.py>
```

## Writing code
Open Terminal and move to the directory
```
cd ~/ros2_ws/src/
code .
```

It will open the vs code and you have to write the code in the vs code for your nodes
and you have to write the code in the created Python Node file like this
```
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
class MyCustomNode(Node):
    def __init__(self):
        super().__init__('my_node_name')
        self.get_logger().info("Hello World") #This Line will print the Info
def main(args=None):
    rclpy.init(args=args)
    node = MyCustomNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()
```

Then get to the setup.py file in the same package and if you scroll down you can able to see entry_points script there type this
entry_points={
        'console_scripts': [
            "test_node = my_py_pkg.my_first_node:main" #Syntax is <executable_name> = <package_name>.<node_name>:<function_name>
        ],
    },

After this we need to build the package
```
cd ~/ros2_ws/
colcon build
```

## Running Node
```
source ~/.bashrc
ros2 run my_py_pkg test_node
```
