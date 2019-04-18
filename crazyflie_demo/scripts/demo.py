#!/usr/bin/env python

import rospy
import math
import tf
import numpy as np
import time
from tf import TransformListener
from geometry_msgs.msg import PoseStamped
#Define class Demo
class Demo():
    def __init__(self, goals):
        rospy.init_node('demo', anonymous=True)
        self.worldFrame = rospy.get_param("~worldFrame", "/world")
        self.frame = rospy.get_param("~frame")
        self.pubGoal = rospy.Publisher('goal', PoseStamped, queue_size=1) #publish to topic goal with msg type PoseStamped
        self.listener = TransformListener() #tflisterner is a method with functions relating to transforms
        self.goals = goals #Assign nX5 matrix containing target waypoints 
        self.goalIndex = 0 # start with the first row of entries (first waypoint)

    def run(self):
        self.listener.waitForTransform(self.worldFrame, self.frame, rospy.Time(), rospy.Duration(5.0)) #Find the transform from world frame to body frame, returns bool on if it can find a transform
        goal = PoseStamped()
        goal.header.seq = 0
        goal.header.frame_id = self.worldFrame
        while not rospy.is_shutdown():
            goal.header.seq += 1
            goal.header.stamp = rospy.Time.now()
            goal.pose.position.x = self.goals[self.goalIndex][0]
            goal.pose.position.y = self.goals[self.goalIndex][1]
            goal.pose.position.z = self.goals[self.goalIndex][2]
            quaternion = tf.transformations.quaternion_from_euler(0, 0, self.goals[self.goalIndex][3])
            goal.pose.orientation.x = quaternion[0]
            goal.pose.orientation.y = quaternion[1]
            goal.pose.orientation.z = quaternion[2]
            goal.pose.orientation.w = quaternion[3]

            self.pubGoal.publish(goal)

            t = self.listener.getLatestCommonTime(self.worldFrame, self.frame)
            if self.listener.canTransform(self.worldFrame, self.frame, t):
                position, quaternion = self.listener.lookupTransform(self.worldFrame, self.frame, t)
                rpy = tf.transformations.euler_from_quaternion(quaternion)
                #If within position error bound, sleep and then move to next waypoint
                if     math.fabs(position[0] - self.goals[self.goalIndex][0]) < 0.2 \
                   and math.fabs(position[1] - self.goals[self.goalIndex][1]) < 0.2 \
                   and math.fabs(position[2] - self.goals[self.goalIndex][2]) < 0.2 \
                   and math.fabs(rpy[2] - self.goals[self.goalIndex][3]) < math.radians(10) \
                   and self.goalIndex < len(self.goals) - 1:
                        rospy.sleep(self.goals[self.goalIndex][4])
                        self.goalIndex += 1
