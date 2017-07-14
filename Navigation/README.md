# Navigation Module:

![screenshot](https://raw.githubusercontent.com/abdalmoniem/Air_and_Land_Firefighting_Agents_-ALFA-/master/Navigation/assets/screenshot_13.png)

Navigation is a corner stone in ALFA's structure, it is divided into two main parts, path planning and path coverage.

1. Path Planning:
	
	path planning is the sub-module that is responsible for moving a robot from its location
	to a target location, which it receives from the master robot, avoiding obstacles, along
	the shortest path and using the least resources. It does so by implementing the
	Advanced Monte Carlo Localization Algorithm or AMCL for short, and although it is
	mainly an adaptive, live, localization algorithm, it implements in its core a path planning
	algorithm using A* which uses a tree like structure to navigate all the nodes of the grid
	of the map and find the shortest distance from its current location to the target
	location.
2. Path Coverage:
	
	path coverage is the action a robot takes once it arrives to its target location. It starts to
	cover an area which its entry point was the target location, it implements a zig-zag
	algorithm to cover all the sub areas of that particular area, this area is partitioned by the
	master robot and the locations of these sub areas are sent to the robots alongside the
	entry point so a robot can traverse these sub-areas using its predefined sub module
	(path planning).


# Advantages of the navigation module:

1. Resource saving.
2. Optimal path finding and coverage.
3. Guaranteed obstacle avoidance.
4. Feedback system that informs the master whether a particular robot has reached
its target and covered its area or not.

## How it works:

relying heavily on the ROS framework, the navigation module works as follows:

1. it listens to `/commander` topic, which other modules (like the task allocation module) might publish to.
2. if it recieves a new message, it identifies the robot id and the location other modules wish this particular robot goes to.
3. publish this point as a goal to the `/amcl` node that in loaclises the robot and then starts moving the robot according to the
	shortest path it found.
4. when the robots reaches the goal, it broadcasts a success message, otherwise, it publishes a failure message and retries again.
5. this process executes in a never ending loop until the robots shutdown or the batteries die.

## Flowchart:
![flowchart](https://raw.githubusercontent.com/abdalmoniem/Air_and_Land_Firefighting_Agents_-ALFA-/master/Navigation/assets/flow_chart.png)

## Packages:
1. multiple_robots_stage:
	
	this is the simulation of the navigation module on two robots, read the `README` of the package to find out how it works

2. pathplanning_turtlebot_stage:

	this is the simulation of the navigation module on one robot, read the `README` of the package to find out how it works