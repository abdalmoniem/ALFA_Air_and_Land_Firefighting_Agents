#!/usr/bin/env python

import rospy
import actionlib

from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


clients = []
total_robots = 2


def navigate(msg):
    points_list = msg.data.split("-")

    for data in points_list:
        point = data.split(",")

        rid = int(point[0])
        x = float(point[1])
        y = float(point[2])

        print "robot_%d is going to (x:%.3f y:%.3f)" % (rid, x, y)
        print

        if rid < len(clients):
            pose = [(x, y, 0.0), (0.0, 0.0, 0.0, 1.0)]
            goal = goal_pose(pose)

            # clients[rid].cancel_all_goals()
            clients[rid].send_goal(goal)
            # clients[rid].wait_for_result()
        else:
            rospy.logerr(
                "invalid robot id, please choose an id between 0 and %d" % (len(clients) - 1))


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

    for i in range(total_robots):
        clients.append(actionlib.SimpleActionClient(
            '/robot_%d/move_base' % i, MoveBaseAction))

    for client in clients:
        client.wait_for_server()

    rospy.spin()
