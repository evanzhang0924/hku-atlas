#!/usr/bin/env python

'''
Created on Monday Jan 1st 09:55 2018

@ Author: ZHANG Yupeng
'''
# Author: ZHANG Yupeng

# How to control the Atlas doing what we want him to do?
# The Atlas Conrol over ROS with Python tutorial has solved this question.
# By creating a topic for publish messages, this python file is used to do it.

import roslib; roslib.load_manifest('tutorial_atlas_control')
import rospy, yaml, sys
from atlas_msgs.msg import AtlasCommand
from sensor_msgs.msg import JointState
from numpy import zeros, array, linspace
from math import ceil

atlasJointNames = [
    'atlas::back_bkz', 'atlas::back_bky', 'atlas::back_bkx', 'atlas::neck_ry',
    'atlas::l_leg_hpz', 'atlas::l_leg_hpx', 'atlas::l_leg_hpy', 'atlas::l_leg_kny', 'atlas::l_leg_aky', 'atlas::l_leg_akx',
    'atlas::r_leg_hpz', 'atlas::r_leg_hpx', 'atlas::r_leg_hpy', 'atlas::r_leg_kny', 'atlas::r_leg_aky', 'atlas::r_leg_akx',
    'atlas::l_arm_shz', 'atlas::l_arm_shx', 'atlas::l_arm_ely', 'atlas::l_arm_elx', 'atlas::l_arm_wry', 'atlas::l_arm_wrx', 'atlas::l_arm_wry2',
    'atlas::r_arm_shz', 'atlas::r_arm_shx', 'atlas::r_arm_ely', 'atlas::r_arm_elx', 'atlas::r_arm_wry', 'atlas::r_arm_wrx', 'atlas::r_arm_wry2']

currentJointState = JointState()
def jointStatesCallback(msg):
    global currentJointState
    currentJointState = msg

if __name__ == '__main__':

    # first make sure the input arguments are correct
    if len(sys.argv) != 3:
        print "usage: traj_yaml.py YAML_FILE TRAJECTORY_NAME"
        print "  where TRAJECTORY is a dictionary defined in YAML_FILE"
        sys.exit(1)
    traj_yaml = yaml.load(file(sys.argv[1], 'r'))
    traj_name = sys.argv[2]
    if not traj_name in traj_yaml:
        print "unable to find trajectory %s in %s" % (traj_name, sys.argv[1])
        sys.exit(1)
    traj_len = len(traj_yaml[traj_name])

    # Setup subscriber to atlas states
    rospy.Subscriber("/atlas/joint_states", JointState, jointStatesCallback)

    # initialize JointCommands message
    command = AtlasCommand()
    # command.name = list(atlasJointNames)
    n = 30
    command.position     = list(zeros(n))
    command.velocity     = list(zeros(n))
    command.effort       = list(zeros(n))
    command.k_effort     = list(zeros(n))
    # command.kp_position  = list(zeros(n))
    # command.ki_position  = zeros(n)
    # command.kd_position  = zeros(n)
    # command.kp_velocity  = zeros(n)
    # command.i_effort_min = zeros(n)
    # command.i_effort_max = zeros(n)

    # now get gains from parameter server
    rospy.init_node('tutorial_atlas_control')
    # ros.get_param('/atlas_controller/gains/l_arm_shz/p')
    # ros.get_param('/atlas_controller/gains/l_arm_shz/p')
    # ros.get_param('/atlas_controller/gains/l_arm_shz/p')
    # ros.get_param('/atlas_controller/gains/l_arm_shz/p')

    # for i in xrange(0, 30):
    #   name = command.name[i]
    #   command.kp_position[i]  = rospy.get_param('/atlas_controller/gains/' + name[7::] + '/p')
    #   command.ki_position[i]  = rospy.get_param('/atlas_controller/gains/' + name[7::] + '/i')
    #   command.kd_position[i]  = rospy.get_param('/atlas_controller/gains/' + name[7::] + '/d')
    #   command.i_effort_max[i] = rospy.get_param('/atlas_controller/gains/' + name[7::] + '/i_clamp')
    #   command.i_effort_min[i] = -command.i_effort_max[i]



    # set up the publisher
    pub = rospy.Publisher('/atlas/atlas_command', AtlasCommand, queue_size=1)

    # for each trajectory
    for i in xrange(0, traj_len):
        # get initial joint positions
        initialPosition = array(currentJointState.position)

        # initialPosition = initialPosition[16:23]
        # get joint commands from yaml
        y = traj_yaml[traj_name][i]

        # first value is time duration
        dt = float(y[0])

        # subsequent values are desired joint positions
        commandPosition = array([ float(x) for x in y[1].split() ])

        # desired publish interval
        dtPublish = 0.02
        n = ceil(dt / dtPublish)
        
        for ratio in linspace(0, 1, n):
            command.k_effort[16:23] = [255] * 7
            interpCommand = (1-ratio)*initialPosition + ratio * commandPosition
            command.position = [ float(x) for x in interpCommand ]
            # print command
            pub.publish(command)
            rospy.sleep(dt / float(n))
