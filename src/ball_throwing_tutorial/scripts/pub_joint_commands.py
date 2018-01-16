#!/usr/bin/env python

# Author: ZHANG Yupeng

# How to control the Atlas doing what we want him to do?
# The Atlas Conrol over ROS with Python tutorial has solved this question.
# By creating a topic for publish messages, this python file is used to do it.

import math
import rospy

from sensor_msgs.msg import JointState
from osrf_msgs.msg import JointCommands
