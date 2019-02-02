#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from counter_and_reset.srv import int_bool

if __name__ == '__main__':
	rospy.init_node("Memin_counter", anonymous=True)
	rospy.wait_for_service("/do_not_make_eleven")
	pub = rospy.Publisher("/increase", Int64, queue_size=10)

	rate = rospy.Rate(1)


	msg = Int64()
	msg.data = 0

	while not rospy.is_shutdown():	
		pub.publish(msg)

		try:
			reset = rospy.ServiceProxy("/do_not_make_eleven",int_bool)
			response = reset(msg.data)
			if response.result == True:
				msg.data = 0
		except rospy.ServiceException as e:
			rospy.logwarn("Service failed: " + str(e))

		msg.data +=1
		rate.sleep()
