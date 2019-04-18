#!/usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import PoseStamped

if __name__ == '__main__':
    rospy.init_node('publish_pose', anonymous=True)
    worldFrame = rospy.get_param("~worldFrame", "/world")
    name = rospy.get_param("~name")
    r = rospy.get_param("~rate")
    x = rospy.get_param("~x")
    y = rospy.get_param("~y")
    z = rospy.get_param("~z")

    rate = rospy.Rate(r)
    #open the text file
	f = open('/home/crazyflie_ws/src/crazyflie_ros/crazyflie_demo/scripts/xypath.txt','r')
	lines = f.readlines()
	f.seek(0,0)
	temp = f.readline()
	temp = temp.split(" ")
    #define message parameters to be published (message contains POSE)
    #Initial condition waypoint
    msg = PoseStamped()
    msg.header.seq = 0
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = worldFrame
    #Now reads from file value (temp)
    msg.pose.position.x = float(temp[0])
    msg.pose.position.y = float(temp[1])  
    #Maintains same z height from launch file arguement (.5m)
    msg.pose.position.z = float(temp[2])  
    quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)
    msg.pose.orientation.x = quaternion[0]
    msg.pose.orientation.y = quaternion[1]
    msg.pose.orientation.z = quaternion[2]
    msg.pose.orientation.w = quaternion[3]

    pub = rospy.Publisher(name, PoseStamped, queue_size=1)
	pub.publish(msg)
	go = 0 # Used to create initial time delay
	epoch = rospy.get_time()
    while not rospy.is_shutdown():
		timediff = rospy.get_time()-epoch 
		if go == 1:
			temp = f.readline()
			if not temp:
				go = 2
				temp = lines[-1] # Go back to beggining of waypoint
			temp = temp.split(" ") # Lets you read the space between points
		elif go == 2:
			temp = lines[-1]
			temp = temp.split(" ")
		else:
			if timediff > 5: # After 5 seconds, go =1 and publish first waypoint
				go = 1
		msg.header.stamp = rospy.Time.now()
		msg.pose.position.x = float(temp[0])
		msg.pose.position.y = float(temp[1])
		msg.pose.position.z = float(temp[2])  
		quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)
		msg.pose.orientation.x = quaternion[0]
		msg.pose.orientation.y = quaternion[1]
		msg.pose.orientation.z = quaternion[2]
		msg.pose.orientation.w = quaternion[3]
		pub.publish(msg)
	rate.sleep()




