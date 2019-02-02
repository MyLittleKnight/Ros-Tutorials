#!/usr/bin/env python
import sys
import rospy
from counter_and_reset.srv import int_bool

def make_zero(num):
	if num.data == 11:
		result = True
	else:
		result = False
	return result



if __name__ == '__main__':
	rospy.init_node("reset_numbers")
	rospy.loginfo("service start")

	reset_service = rospy.Service("do_not_make_eleven",int_bool,make_zero)
	rospy.spin()
