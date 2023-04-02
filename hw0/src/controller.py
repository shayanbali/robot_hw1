#!/usr/bin/python3

import rospy
from std_msgs.msg import String
from hw0.msg import proximity
from hw0.msg import direction

def callback(data):
    degree = 0
    rotate_direction = 0 # 1: clockwise  -1: counter clockwise   0:fixed
    rospy.loginfo(rospy.get_caller_id() + '\nreceived ditances: %s', data)
    distance_list = []
    distance_list.append(data.up)
    distance_list.append(data.down)
    distance_list.append(data.left)
    distance_list.append(data.right)
    max_distance = distance_list.index(min(distance_list))
    if max_distance == 0:
        degree = 180
        rotate_direction = 1
    elif max_distance == 2:
        degree = 90
        rotate_direction = 1
    elif max_distance == 3:
        degree = 90
        rotate_direction = -1

    pub1 = rospy.Publisher("motor1", direction, queue_size=10)
    pub2 = rospy.Publisher("motor2", direction, queue_size=10)

    msg = direction()
    msg.degree = degree
    msg.rotate = rotate_direction

    rospy.loginfo("\npublished rotation: \n %s", msg)
    pub1.publish(msg)
    pub2.publish(msg)

    

    



def listener():

    rospy.init_node('controller', anonymous=True)

    rospy.Subscriber('distance', proximity, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()