#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Point

def gpsPub():
	pub = rospy.Publisher('gpsPoint', Point, queue_size=10)
	rospy.init_node('gpsNode', anonymousTrue)
	rate = rospy.Rate(10) # hz
	while not rospy.is_shutdown():
		gpsLoc = gpsRead()
		rospy.loginfo(gpsLoc)
		pub.publish(gpsLoc)
		rate.sleep()

#UNIMPLEMENTED
def pgsRead():
	#READS GPS OUTPUT FROM CORRESPONDING COMMUNICATION PROTOCOL VIA SERIAL / SERIAL ARDUINO / ETC
	#RETURNS A ROS Point OBJECT CONTAINING THE COORDINATES

if __name__ == '__main__':
	try:
		gpsPub()
	except rospy.ROSInterruptException:
		pass