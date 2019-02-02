#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from counter_and_reset.srv import int_bool

def printNum(msg):
	number_info = ""	

	rospy.wait_for_service("/do_not_make_eleven")

	try:
		reset = rospy.ServiceProxy("/do_not_make_eleven",int_bool)
		response = reset(msg.data)
		if response.result == True:
			msg.data = 0
	except rospy.ServiceException as e:
		rospy.logwarn("Service failed: " + str(e))

	if msg.data %2 == 0:
		number_info = "even"
	else:
		number_info = "odd"
	last_message = str(msg.data) + " is " +  number_info
	print(last_message)



if __name__ == '__main__':
	rospy.init_node("print_node")

	sub = rospy.Subscriber("/increase",Int64, printNum)

	rospy.spin()
