#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Point, Accel, Pose, Twist, PoseWithCovariance, TwistWithCovariance
from sensor_msgs import Imu, JointState
from nav_msgs import Odometry

#Point - points
#Accel - free space linear and angular acceleration (Vector3)
#Pose - 3D position (point) and orientation (Quaternion)
#Twist - free space linear and angular velocity (Vector3)

#IMU - stores orientation (Quaternion), angular_velocity (Vector3), and linear_acceleration (Vector3)
#JointState - stores position (float), velocity (float), and effort (float) of a torque-controlled joint
#Odomotry - stores Pose with covariance and Twist with covariance

def statePub():
	odomPub = rospy.Publisher('stateOdometry', Odometry, queue_size=10)
	accelPub = rospy.Publisher('stateAcceleration', Accel, queue_size=10)
	jointPub = rospy.Publisher('stateSteering', JointState, queue_size=10)

	rospy.init_node('stateOdometry', anonymousTrue)
	rospy.init_node('stateAcceleration', anonymousTrue)
	rospy.init_node('stateSteering', anonymousTrue)

	rate = rospy.Rate(10) #hz

	while not rospy.is_shutdown():
		carOdom = getOdomotry()
		carAccel = getAccel()
		carSteer = getSteering()

		rospy.loginfo(carOdom)
		rospy.loginfo(carAccel)
		rospy.loginfo(carSteer)

		odomPub.publish(carOdom)
		accelPub.publish(carAccel)
		jointPub.publish(carSteer)

		rate.sleep()

#UNIMPLEMENTED
def pullSensors():
	#reads sensor information from available nodes, using checkSensors to avoid reading nonexistent nodes
	#stores sensor readings as local variables for getOdometry/getAccel/getSteering to do math with
		#Nodes are only to be read ONCE during a loop to avoid desync issues

def getOdometry():
	#uses relevant sensor data
	#returns a nav_msgs.Odometry object

def getAccel():
	#uses relevant sensor data
	#returns a geometry_msgs.msg.Point object

def getSteering():
	#uses relevant sensor data
	#returns a sensor_msgs.JointState object

def checkSensors():
	#Verifies which sensors are available and sets corresponding flags

if __name__ == '__main__':
	try:
		statePub():
	except rospy.ROSInterruptException:
		pass