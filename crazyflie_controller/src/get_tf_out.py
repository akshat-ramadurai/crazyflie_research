#!/usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import TransformStamped
if __name__ == '__main__':
	rospy.init_node('get_tf_out')
	
	listener = tf.TransformListener()
	rate = rospy.Rate(30.0)
	while not rospy.is_shutdown():
		print('It\'s working')
		try:
			(trans,rot) = listener.lookupTransform('/world', '/vicon/crazyflie2/crazyflie2', rospy.Time(0))
		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			continue
			f = open('~/crazyflie_ws/pos.txt','a')
			f.write('%.6f %.6f %.6f\n' % (trans[0],trans[1],trans[2]))
			f.close()
			


		rate.sleep()