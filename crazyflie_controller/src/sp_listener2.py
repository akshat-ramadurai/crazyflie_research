#!/usr/bin/env python 
import rospy  
from geometry_msgs.msg import Point

#rospy.init_node('A_listener2', anonymous=True)
#epocht = rospy.get_time()  

def write_to(str,t,x,y):
  f = open(str,'a')
  f.write('%.6f %.6f %.6f\n' % (t,x,y))
  f.close()


def callback(msg):
  x = msg.x
  y = msg.y
  epoch = rospy.get_time()- 1551570980.098825
  write_to(rospy.get_param('~write_path'),epoch,x,y)
  #rospy.sleep(.1)
  #rospy.loginfo('time: {}'.format(epoch))

def main():
  rospy.init_node('A_listener2', anonymous=True)
  rospy.Subscriber("/crazyflie2/des_attitude",Point,callback)
  rospy.spin()

if __name__ == '__main__':
  main()
