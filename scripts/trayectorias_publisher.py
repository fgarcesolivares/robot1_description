#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
  
def __init__(self):
        rospy.init_node('/robot1_description/joint1_position_controller')
        self.msg = None
       
       
        self.r_pub = rospy.Publisher('/robot1_description/joint1_position_controller/command',
                Float64,
                queue_size=10)
   
   if __name__ == '__main__':
       try:
           talker()
       except rospy.ROSInterruptException:
           pass
           

