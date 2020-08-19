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
    dir_mask=0
    dir_mask_tmp=15

    if time.time()-last_tag>timeout:
        msg.linear.x = 0
        msg.angular.z = 0
    elif status.status=="outside" or status.status=="unknown":
        msg.linear.x = 0
        msg.angular.z = 0
    elif status.status == "controlled":

        if status.pose_mask & BigBrother.POSE_N:
            dir_mask |= BigBrother.DIR_3
            dir_mask |= BigBrother.DIR_2
        elif status.pose_mask & BigBrother.POSE_S:
            dir_mask |= BigBrother.DIR_4
            dir_mask |= BigBrother.DIR_1

        if dir_mask: 
            dir_mask_tmp=dir_mask

        if status.pose_mask & BigBrother.POSE_E:
            dir_mask=0
            dir_mask |= BigBrother.DIR_4
            dir_mask |= BigBrother.DIR_3
        elif status.pose_mask & BigBrother.POSE_W:
            dir_mask=0
            dir_mask |= BigBrother.DIR_1
            dir_mask |= BigBrother.DIR_2

        dir_mask&=dir_mask_tmp

        print dir_mask
        if not status.direction & dir_mask and msg.linear.x>0:
            msg.linear.x=0
        elif not status.direction<<2 & dir_mask and not status.direction>>2 & dir_mask and msg.linear.x<0:
            msg.linear.x=0
            
        
    pub_cmd.publish(msg)


def callback_status(data):
    global last_tag
    global status

    last_tag = time.time()
    status = data


rospy.init_node('big_brother_control')

timeout = rospy.get_param("~timeout", 1.0)

rospy.loginfo("Int: %s", timeout), 

try:
    sub_status = rospy.Subscriber("big_brother/leo_status", BigBrother, callback_status)
    sub_cmd = rospy.Subscriber("big_brother/cmd_vel", Twist, callback_cmd)
    pub_cmd = rospy.Publisher("cmd_vel", Twist, queue_size=10)

except rospy.ROSInterruptException as e:
	rospy.logerr(e)

rospy.spin()


	