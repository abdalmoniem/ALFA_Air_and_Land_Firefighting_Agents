#!/usr/bin/env python

import rospy
import actionlib

from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


def navigate(msg):
    point = msg.data.split(",")

    x = float(point[0])
    y = float(point[1])

    print "sending the robot to (x:%.3f y:%.3f)" % (x, y)
    print

    pose = [(x, y, 0.0), (0.0, 0.0, 0.0, 1.0)]
    goal = goal_pose(pose)

    # client.cancel_all_goals()
    client.send_goal(goal)
    # client.wait_for_result()


def goal_pose(pose):
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = 'map'
    goal_pose.target_pose.pose.position.x = pose[0][0]
    goal_pose.target_pose.pose.position.y = pose[0][1]
    goal_pose.target_pose.pose.position.z = pose[0][2]
    goal_pose.target_pose.pose.orientation.x = pose[1][0]
    goal_pose.target_pose.pose.orientation.y = pose[1][1]
    goal_pose.target_pose.pose.orientation.z = pose[1][2]
    goal_pose.target_pose.pose.orientation.w = pose[1][3]

    return goal_pose


if __name__ == '__main__':
    rospy.init_node('navigator')

    rospy.Subscriber('/commander', String, navigate)

    rospy.loginfo(
        "navigator node has been started and is listening on /commander topic.")

    client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)

    client.wait_for_server()

    rospy.spin()
