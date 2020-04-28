#!/usr/bin/env python
import math
import rospy
import time
from leo_big_brother.msg import BigBrother
from geometry_msgs.msg import Twist

last_tag=0.0
on_time=False
status = BigBrother()

def callback_cmd(data):
    global status
    msg = data

    if status.status=="inside":
        pass
    # elif status.status=="unknown" or status.status=="outside":
    elif status.status=="outside":
        msg.linear.x = 0
        msg.angular.z = 0
    elif status.status == "controlled":
        if status.location == status.direction:
            if msg.linear.x >= 0: msg.linear.x=0
        else:
            if msg.linear.x <= 0: msg.linear.x=0 
        
    pub_cmd.publish(msg)
    # print msg


def callback_status(data):
    global last_tag
    global status

    last_tag = time.time()
    status = data


try:
    rospy.init_node('big_brother_control')
    sub_status = rospy.Subscriber("big_brother/leo_status", BigBrother, callback_status)
    sub_cmd = rospy.Subscriber("cmd_vel", Twist, callback_cmd)
    pub_cmd = rospy.Publisher("big_brother/cmd_vel", Twist, queue_size=10)

except rospy.ROSInterruptException as e:
	rospy.logerr(e)

rospy.spin()


	