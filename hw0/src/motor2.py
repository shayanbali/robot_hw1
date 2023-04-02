#!/usr/bin/python3

import rospy
from hw0.msg import direction

def callback(data):
    rt = "clockwise"
    if data.rotate == -1:
        rt = "counter clockwise"
    elif data.rotate == 0:
        rt = "fixed"
    rospy.loginfo(rospy.get_caller_id() + '\n%s ' + rt, data)

def listener():

    rospy.init_node('motor22', anonymous=True)

    rospy.Subscriber('motor2', direction, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()