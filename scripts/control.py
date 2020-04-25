#!/usr/bin/env python
import math
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback_cmd(data):
	print(data)
    
def callback_status(data):
	print(data)


try:
    rospy.init_node('big_brother_control')
    sub_status = rospy.Subscriber("big_brother/leo_status", String, callback_status)
    sub_cmd = rospy.Subscriber("cmd_vel", Twist, callback_cmd)
    pub_cmd = rospy.Publisher("big_brother/cmd_vel", Twist, queue_size=10)

except rospy.ROSInterruptException as e:
	rospy.logerr(e)

rospy.spin()


	