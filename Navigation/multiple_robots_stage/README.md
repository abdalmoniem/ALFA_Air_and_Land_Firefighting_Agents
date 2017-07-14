# Multiple Robots in Stage

This is a simulation of the navigation module on two robots, it simulates the system on RVIZ and Stage Robot Simulator.

## How to run it:
	
To start with two robots call `roslaunch multiple_robots_stage robots_in_stage.launch`. This will set two robots in the map.

To give a goal to robot_0 you can call:

`rostopic pub /robot_0/move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: "/map"}, pose: {position: {x: 6.0, y: 1.0, z: 0.0}, orientation: {w: 1.0}}}'`

To give a goal to robot_1 you can call:

`rostopic pub /robot_1/move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: "/map"}, pose: {position: {x: 6.0, y: 2.0, z: 0.0}, orientation: {w: 1.0}}}'`

Alternatively you can run the two nodes `navigator` and `commander` to set goal points more easily:

1. run `rosrun multiple_robots_stage navigator.py` in a terminal, it will inform you that it has been started.
2. run `rosrun multiple_robots_stage commander.py` in another terminal, it receives input in the following format:

	(goal to robot_0)-(goal to robot_1)-(goal to robot_2)-...etc

	for example:

	`id_0, x1, y1 - id_1, x2, y2 - id_2, x3, y3, etc...`

	or more specifically:

	`0, 6, 1 - 1, 6, 2`

	this will set the goal of robot_0 to the point (6, 1) and the goal of robot_1 to the point (6, 2)
