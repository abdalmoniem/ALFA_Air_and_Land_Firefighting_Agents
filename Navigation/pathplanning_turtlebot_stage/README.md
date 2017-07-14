# Pathplanning Turtlebot Stage

This is a simulation of the navigation module on one robot, it simulates the system on RVIZ and Stage Robot Simulator.

## How to run it:
	
To start with two robots call `roslaunch pathplanning_turtlebot_stage turtlebot_in_stage.launch`. This will set two robots in the map.

To give a goal to the robot you can call:

`rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: "/map"}, pose: {position: {x: 6.0, y: 1.0, z: 0.0}, orientation: {w: 1.0}}}'`

Alternatively you can run the two nodes `navigator` and `commander` to set goal points more easily:

1. run `rosrun pathplanning_turtlebot_stage navigator.py` in a terminal, it will inform you that it has been started.
2. run `rosrun pathplanning_turtlebot_stage commander.py` in another terminal, it receives input in the following format:

	`(goal to robot)`

	for example:

	`x, y`

	or more specifically:

	`6, 1`

	this will set the goal of the robot to the point `(6, 1)`
