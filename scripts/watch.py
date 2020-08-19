#!/usr/bin/env python
import math
import rospy
from leo_big_brother.msg import BigBrother
from ar_track_alvar_msgs.msg import AlvarMarkers
from tf.transformations import euler_from_quaternion

def callback_marker(data):
	msg=BigBrother()
	pose_mask=0

	try:
		position=data.markers[0].pose.pose.position

		orientation_quat=data.markers[0].pose.pose.orientation
		orientation_list = [orientation_quat.x, orientation_quat.y, orientation_quat.z, orientation_quat.w]
		orientation = euler_from_quaternion(orientation_list)
		angle=orientation[2]


		if abs(position.x)<=width/2.0 and abs(position.y)<=height/2.0: msg.status="inside"
		elif abs(position.x)>=(width/2.0)+thickness or abs(position.y)>=(height/2.0)+thickness: msg.status="outside"
		else: 
			msg.status="controlled"

			if position.x>=width/2:
				pose_mask |= BigBrother.POSE_N
			elif position.x<=-width/2:
				pose_mask |= BigBrother.POSE_S
			
			if position.y>=height/2:
				pose_mask |= BigBrother.POSE_E
			elif position.y<=-height/2:
				pose_mask |= BigBrother.POSE_W

			if angle < math.pi/2 and angle >=0:
				msg.direction=BigBrother.DIR_1
			elif angle >=math.pi/2 and angle < math.pi:
				msg.direction=BigBrother.DIR_2
			elif angle <-math.pi/2 and angle >=-math.pi:
				msg.direction=BigBrother.DIR_3
			elif angle >=-math.pi/2 and angle <=0:
				msg.direction=BigBrother.DIR_4

			msg.pose_mask=pose_mask

		pub_status.publish(msg)

	except: 
		msg.status="unknown"
		pub_status.publish(msg)


rospy.init_node('big_brother_watch')

height = rospy.get_param("~safe_zone_height", 0.5)
width = rospy.get_param("~safe_zone_width", 0.5)
thickness = rospy.get_param("~controlled_zone_thickness", 0.2)


rospy.loginfo("Int: %s,Int: %s,Int: %s", height , width, thickness)

try:
	pub_status = rospy.Publisher("big_brother/leo_status", BigBrother, queue_size=10)
	sub_marker = rospy.Subscriber('ar_pose_marker', AlvarMarkers, callback_marker)
except rospy.ROSInterruptException as e:
	rospy.logerr(e)

rospy.spin()


	