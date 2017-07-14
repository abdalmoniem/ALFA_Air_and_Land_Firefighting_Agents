#!/usr/bin/env python
import rospy

from std_msgs.msg import String

rospy.init_node('commander')
pub = rospy.Publisher('/commander', String, queue_size=100)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    msg = String()
    user_input = raw_input(
        "Enter a coordinate (in the form \"x, y\") for the robot to seek: ")

    if user_input == "quit" or user_input == "exit":
        print "aye aye sir, see ya"
        exit(0)
    msg.data = user_input
    pub.publish(msg)
    rate.sleep()
