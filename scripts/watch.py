#!/usr/bin/env python
import math
import time
import rospy
from geometry_msgs.msg import Twist
from ar_track_alvar_msgs.msg import AlvarMarkers
from tf.transformations import euler_from_quaternion

position=None
angle=None

last_callback=0.0
refresh_time=5

is_available=False


def callback_marker(data):
	global position
	global angle

	global last_callback
	global is_available

	if time.time()-last_callback>refresh_time:
		is_available=False
	else: is_available=True

	try:
		position=data.markers[0].pose.pose.position

		orientation_quat=data.markers[0].pose.pose.orientation
		orientation_list = [orientation_quat.x, orientation_quat.y, orientation_quat.z, orientation_quat.w]
		orientation = euler_from_quaternion(orientation_list)
		angle=orientation[2]
		print (orientation, angle)

		last_callback=time.time()

	except: return


if __name__ == "__main__":
	try:
		rospy.init_node('go_to_goal')
		pub_cmd = rospy.Publisher("big_brother/cmd_vel", Twist, queue_size=10)
		sub_marker = rospy.Subscriber('ar_pose_marker', AlvarMarkers, callback_marker)
	except rospy.ROSInterruptException as e:
		rospy.logerr(e)

	rospy.spin()


	