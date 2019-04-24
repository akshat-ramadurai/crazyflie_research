#!/usr/bin/env python 
import rospy 
from geometry_msgs.msg import Twist 


def write_to(str,t,x,y,z):
  f = open(str,'a')
  f.write('%.6f %.6f %.6f %.6f\n' % (t,x,y,z))
  f.close()
def callback(msg):
  x = msg.linear.x
  y = msg.linear.y
  epoch = rospy.get_time()-1556062300
  write_to("pos.txt",epoch,x,y,0)
  rospy.sleep(.15)
  rospy.loginfo('time: {}'.format(epoch))

def main():
  rospy.init_node('A_listener', anonymous=True)
  rospy.Subscriber("/crazyflie2/cmd_vel",Twist,callback)
  rospy.spin()

if __name__ == '__main__':
  main()







"""
import rospy
from geometry_msgs.msg import Twist
 
def callback(data):
 rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
     
def listener():
  print("Hello nom")
 # In ROS, nodes are uniquely named. If two nodes with the same
 # name are launched, the previous one is kicked off. The
 # anonymous=True flag means that rospy will choose a unique
 # name for our 'listener' node so that multiple listeners can
 # run simultaneously.
  rospy.init_node('A_listener', anonymous=True)
  
  rospy.Subscriber("/crazyflie4/cmd_vel", Twist, callback)
  try:
    print(callback.linear.x)
  # spin() simply keeps python from exiting until this node is stopped
  

  rospy.spin(10)
   
if __name__ == '__main__':
 listener()
"""