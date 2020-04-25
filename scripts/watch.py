#!/usr/bin/env python
import math
import rospy
from std_msgs.msg import String
from ar_track_alvar_msgs.msg import AlvarMarkers
from tf.transformations import euler_from_quaternion

def callback_marker(data):
	global height
	global width
	global thickness
	msg=String()

	try:
		position=data.markers[0].pose.pose.position

		orientation_quat=data.markers[0].pose.pose.orientation
		orientation_list = [orientation_quat.x, orientation_quat.y, orientation_quat.z, orientation_quat.w]
		orientation = euler_from_quaternion(orientation_list)
		angle=orientation[2]

		if abs(position.x)<=width/2.0 and abs(position.y)<=height/2.0: msg="in"
		elif abs(position.x)>=(width/2.0)+thickness or abs(position.y)>=(height/2.0)+thickness: msg="out"
		else: msg="controlled"
		# TODO rover status in mid area

		pub_status.publish(msg)
		print(msg)

	except: 
		msg="unknown"
		pub_status.publish(msg)




height = rospy.get_param("/height", 0.5)
width = rospy.get_param("/width", 0.5)
thickness = rospy.get_param("/thickness", 0.1)
rospy.loginfo("Int: %s,Int: %s,Int: %s", height , width, thickness)


try:
	rospy.init_node('big_brother_watch')
	pub_status = rospy.Publisher("big_brother/leo_status", String, queue_size=10)
	sub_marker = rospy.Subscriber('ar_pose_marker', AlvarMarkers, callback_marker)
except rospy.ROSInterruptException as e:
	rospy.logerr(e)

rospy.spin()


	