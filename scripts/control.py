#!/usr/bin/env python
import math
import rospy
import time
from std_msgs.msg import String
from geometry_msgs.msg import Twist

last_tag=0.0
is_leo=False
status_leo="unknown"

def callback_cmd(data):
    global status_leo

    msg = data

    if status_leo=="unknown" or status_leo=="out":
        msg.x = 0
        msg.z = 0

    pub_cmd.publish(msg)


def callback_status(data):
    global last_tag
    global status_leo

    last_tag = time.time()
    status_leo = data.data


try:
    rospy.init_node('big_brother_control')
    sub_status = rospy.Subscriber("big_brother/leo_status", String, callback_status)
    sub_cmd = rospy.Subscriber("cmd_vel", Twist, callback_cmd)
    pub_cmd = rospy.Publisher("big_brother/cmd_vel", Twist, queue_size=10)

except rospy.ROSInterruptException as e:
	rospy.logerr(e)

rospy.spin()


	