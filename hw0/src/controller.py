#!/usr/bin/python3

import rospy
from std_msgs.msg import String
from hw0.msg import proximity
from hw0.msg import direction

state = "N"

def callback(data):
    global state
    degree = 0
    rotate_direction = 0 # 1: clockwise  -1: counter clockwise   0:fixed
    rospy.loginfo(rospy.get_caller_id() + '\nreceived ditances: %s\nState before rotation: '+state, data)
    distance_list = []
    distance_list.append(data.up)
    distance_list.append(data.down)
    distance_list.append(data.left)
    distance_list.append(data.right)
    max_distance = distance_list.index(min(distance_list))
    if max_distance == 0:
        degree = 180
        rotate_direction = 1
        if state == "N":
            state = "S"
        elif state == "E":
            state = "W"
        elif state == "S":
            state = "N"
        elif state == "W":
            state = "E"
        
    elif max_distance == 2:
        degree = 90
        rotate_direction = 1
        if state == "N":
            state = "E"
        elif state == "E":
            state = "S"
        elif state == "S":
            state = "W"
        elif state == "W":
            state = "N"

    elif max_distance == 3:
        degree = 90
        rotate_direction = -1
        if state == "N":
            state = "W"
        elif state == "E":
            state = "N"
        elif state == "S":
            state = "E"
        elif state == "W":
            state = "S"

    pub1 = rospy.Publisher("motor1", direction, queue_size=10)
    pub2 = rospy.Publisher("motor2", direction, queue_size=10)

    msg = direction()
    msg.degree = degree
    msg.rotate = rotate_direction

    rospy.loginfo("\npublished rotation: \n %s\nState after rotation: "+state, msg)
    pub1.publish(msg)
    pub2.publish(msg)

    

    



def listener():

    rospy.init_node('controller', anonymous=True)

    rospy.Subscriber('distance', proximity, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()