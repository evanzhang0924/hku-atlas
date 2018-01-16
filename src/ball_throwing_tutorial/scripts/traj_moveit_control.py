#!/usr/bin/env python

# Author: ZHANG Yupeng

# How to control the Atlas doing what we want him to do?
# The Atlas Conrol over ROS with Python tutorial has solved this question.
# By creating a topic for publish messages, this python file is used to do it.

import roslib; roslib.load_manifest('ball_throwing_tutorial')
import rospy
import yaml
import sys

from osrf_msgs.msg import JointCommands
from sensor_msgs.msg import JointState
from numpy import zeros, array, linspace
from math import ceil

atlasJointNames = [
  'atlas::back_lbz', 'atlas::back_mby', 'atlas::back_ubx', 'atlas::neck_ay',
  'atlas::l_leg_uhz', 'atlas::l_leg_mhx', 'atlas::l_leg_lhy', 'atlas::l_leg_kny', 'atlas::l_leg_uay', 'atlas::l_leg_lax',
  'atlas::r_leg_uhz', 'atlas::r_leg_mhx', 'atlas::r_leg_lhy', 'atlas::r_leg_kny', 'atlas::r_leg_uay', 'atlas::r_leg_lax',
  'atlas::l_arm_usy', 'atlas::l_arm_shx', 'atlas::l_arm_ely', 'atlas::l_arm_elx', 'atlas::l_arm_uwy', 'atlas::l_arm_mwx',
  'atlas::r_arm_usy', 'atlas::r_arm_shx', 'atlas::r_arm_ely', 'atlas::r_arm_elx', 'atlas::r_arm_uwy', 'atlas::r_arm_mwx']

currentJointState = JointState()

def jointStatesCallback(msg):
    global currentJointState
    currentJointState = msg

if __name__ == '__main__':

    # First of all, it is important to check that the input arguments are correct
    if len(sys.argv) != 3:
        print "usage: traj_moveit_control.py YAML_FILE TRAJECTORY_NAME"
        print "     where TRAJECTORY is a dictionary defined in YAML_FILE"
        sys.exit(1)
    traj_yaml = yaml.load(file(sys.argv[1], 'r'))
    traj_name = sys.argv[2]
    if not traj_name in traj_yaml:
        print "unable to find trajectory %s in %s" % (traj_name, sys.argv[1])
        sys.exit(1)
    traj_len = len(traj_yaml[traj_name])

    # Setup subscriber to atlas states
    rospy.Subscriber("/atlas/joint_states", JointState, jointStatesCallback)

    # Initialize JointCommands messages
    command = JointCommands()
    command.name = list(atlasJointNames)
    n = len(command.name)
    command.position     = zeros(n)
    command.velocity     = zeros(n)
    command.effort       = zeros(n)
    command.kp_position  = zeros(n)
    command.ki_position  = zeros(n)
    command.kd_position  = zeros(n)
    command.kp_velocity  = zeros(n)
    command.i_effort_min = zeros(n)
    command.i_effort_max = zeros(n)

    # Now, get gains from parameter server
    rospy.init_node('ball_throwing_tutorial')
    for i in xrange(len(command.name)):
        name = command.name[i]
        command.kp_position[i]  = rospy.get_param('atlas_controller/gains/' + name[7::] + '/p')
        command.ki_position[i]  = rospy.get_param('atlas_controller/gains/' + name[7::] + '/i')
        command.kd_position[i]  = rospy.get_param('atlas_controller/gains/' + name[7::] + '/d')
        command.i_effort_max[i] = rospy.get_param('atlas_controller/gains/' + name[7::] + '/i_clamp')
        command.i_effort_min[i] = -command.i_effort_max[i]

    # Setup the publisher
    pub = rospy.Publisher('/atlas/joint_commands', JointCommands, queue_size = 1)

    # For each trajectory
    for i in xrange(0, traj_len):

        # Get initial joint positions
        initialPosition = array(currentJointState.position)

        # Get joint commands from yaml
        y = traj_yaml[traj_name][i]

        # First value is time duration
        dt = float(y[0])

        # Subsequent values are desired joint positions
        commandPosition = array([ float(x) for x in y[1].split() ])

        # Desired publish interval
        dtPublish = 0.02
        n = ceil(dt / dtPublish)
        for ratio in linspace(0, 1, n):
            interpCommand = (1 - ration) * initialPosition + ratio * commandPosition
            cmmand.position = [ float(x) for x in interpCommand ]
            pub.publish(command)
            rospy.sleep(dt / float(n))
