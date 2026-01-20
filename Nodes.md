# Node

## Demo Node
```
ros2 run demo_nodes_cpp talker 
```
```
ros2 run demo_nodes_cpp listener
```
```
rqt_graph 
```
## Turtle Node

```
ros2 run turtlesim turtlesim_node
```
```
ros2 run turtlesim turtle_teleop_key
```
```
rqt_graph
```

# Topics
```
ros2 topic list
```
```
ros2 topic info <topic_name>
```
```
ros2 interface show <interface_name>
```

# Services
```
ros2 service list
```
```
ros2 service type <service_name>
```
```
ros2 interface show <interface_name>
```
```
ros2 service call <service_name> <interface_name> "{request}"
```

# Actions
```
ros2 action list
```
```
ros2 action info <action_name>
```
```
ros2 interface show <interface_show>
```
```
ros2 action send_goal <action_name> <interface_name> "{goal}"
```

# Parameters
```
ros2 param list
```
```
ros2 param get <node_name><param_name>
```
```
ros2 run turtlesim turtlesim_node --ros-args -p background_b:=0 -p background_r:=0
```

# Launch
```
ros2 run <package_name> <launch_file>
```
```
ros2 launch demo_nodes_cpp talker_listener_launch.py
```
```
ros2 node list
```
```
ros2 launch turtlesim multisim.launch.py
```
```
ros2 node list
```