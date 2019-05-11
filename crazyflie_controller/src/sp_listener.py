#!/usr/bin/env python 
import rospy 
from geometry_msgs.msg import Twist 
from geometry_msgs.msg import Point

   
#rospy.init_node('A_listener', anonymous=True)
#epocht = rospy.get_time()  

def write_to(str,t,x,y,z):
  f = open(str,'a')
  f.write('%.6f %.6f %.6f %.6f\n' % (t,x,y,z))
  f.close()

def callback(msg):
  x = msg.linear.x # Roll command 
  y = msg.linear.y #Pitch
  z = msg.linear.z #Thrust
  epoch = rospy.get_time()-1551570980.098825    
  write_to(rospy.get_param('~write_path'),epoch,x,y,z)
  #rospy.sleep(.1)
  #rospy.loginfo('time: {}'.format(epocht))


def main():
  rospy.init_node('A_listener', anonymous=True)
  rospy.Subscriber("/crazyflie2/cmd_vel",Twist,callback)
  rospy.spin()

if __name__ == '__main__':
  main()


