#!/usr/bin/env python

'''
Created on Monday Jan 1st 09:55 2018

@ Author: ZHANG Yupeng
'''
# Author: ZHANG Yupeng

# How to control the Atlas doing what we want him to do?
# The Atlas Conrol over ROS with Python tutorial has solved this question.
# By creating a topic for publish messages, this python file is used to do it.

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

import roslib; roslib.load_manifest('tutorial_atlas_control')
from atlas_msgs.msg import AtlasCommand
from sensor_msgs.msg import JointState
from std_msgs.msg import String
from numpy import zeros, array, linspace
from math import ceil

atlasJointNames = [
    'atlas::back_bkz', 'atlas::back_bky', 'atlas::back_bkx', 'atlas::neck_ry',
    'atlas::l_leg_hpz', 'atlas::l_leg_hpx', 'atlas::l_leg_hpy', 'atlas::l_leg_kny', 'atlas::l_leg_aky', 'atlas::l_leg_akx',
    'atlas::r_leg_hpz', 'atlas::r_leg_hpx', 'atlas::r_leg_hpy', 'atlas::r_leg_kny', 'atlas::r_leg_aky', 'atlas::r_leg_akx',
    'atlas::l_arm_shz', 'atlas::l_arm_shx', 'atlas::l_arm_ely', 'atlas::l_arm_elx', 'atlas::l_arm_wry', 'atlas::l_arm_wrx', 'atlas::l_arm_wry2',
    'atlas::r_arm_shz', 'atlas::r_arm_shx', 'atlas::r_arm_ely', 'atlas::r_arm_elx', 'atlas::r_arm_wry', 'atlas::r_arm_wrx', 'atlas::r_arm_wry2']

def atlas_move_python():

    # Print out the message setup notice
    print "====================Starting setup process========================"

    # Initialize the roscpp_initialize
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('atlas_move_python', anonymous=True)


    # Instantiate a RobotCommander object, which is an interface to
    # the robot itself as a whole.
    robot = moveit_commander.RobotCommander()


    # Instantiate a PlanningSceneInterface object, which is an interface to
    # the world file surrounding the Atlas robot.
    scene = moveit_commander.PlanningSceneInterface()


    # Instantiate a MoveGroupCommander object, which is an interface to one
    # group of joints.
    # Of course, I plan to use the left arm as the joint to catch the ball.
    # This interface can be used to plan & execute motions on the left arm.
    group = moveit_commander.MoveGroupCommander("left_arm")

    # Create a DisplayTrajectory publisher which is used to publish trajectories
    # for RVIZ to visualize.
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size = 20)

    # Launch the RVIZ and wait it initialize.
    print "====================Launch the RVIZ========================"
    rospy.sleep(10)
    print "====================Launch completion========================"


    # Getting basic Information.

    print "============= Reference frame: %s" % group.get_planning_frame()

    print "============= End effector: %s" % group.get_end_effector_link()

    print "============= Robot Groups:"
    print robot.get_group_names()


    # For debugging reasons, it is useful to print the entire state of the robot.
    print "============= Printing robot state"
    print robot.get_current_state()
    print "============= Robot state printing finished."


    # Planning to a pose goal
    print "============= Generating plan 1"
    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.w = 1.0
    pose_target.position.x = 0.5
    pose_target.position.y = 0.5
    pose_target.position.z = 0.5
    group.set_pose_target(pose_target)
    print "============= Plan 1 has been generated!"

    # Until now, I have set the target pose, it is time to call the planner
    # to compute the plan and visualize it if successful.
    # It is important to note that I just start planning, not asking the Atlas
    # to actually move its joint.
    plan1 = group.plan()


    print "============= Waiting while RVIZ displays plan1..."
    rospy.sleep(5)

    print "============ STOPPING"

    time_duration = 3 / len(plan1.joint_trajectory.points)
    trajectories = []










trajectories = [[0.25, "0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0 0  0 0 0 0 0 0 0"],
             [0.25, "0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  -0.167 0.33 0.833 0.667 0.7 -0.5 -0.767  0 0 0 0 0 0 0"],
             [0.25, "0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  -0.335 0.67 1.667 1.333 1.4 -1.0 -1.533  0 0 0 0 0 0 0"],
             [0.25, "0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  -0.5 1.0 2.5 2.0 2.1 -1.5 -2.3  0 0 0 0 0 0 0"]]


currentJointState = JointState()
def jointStatesCallback(msg):
    global currentJointState
    currentJointState = msg

if __name__ == '__main__':

    # Generate the trajectories
    try:
        atlas_move_python()
    except rospy.ROSInterruptException:
        pass

    # first make sure the input arguments are correct
    if len(sys.argv) != 1:
        print "usage: python pub_joint_commands.py"
        print "notice: other scripts are written inside pub_joint_commands.py"
        sys.exit(1)

    # traj_yaml = yaml.load(file(sys.argv[1], 'r'))
    traj_test = trajectories

    # traj_name = sys.argv[2]

    # if not traj_name in traj_yaml:
    #     print "unable to find trajectory %s in %s" % (traj_name, sys.argv[1])
    #     sys.exit(1)

    traj_len = len(traj_test)

    # Setup subscriber to atlas states
    rospy.Subscriber("/atlas/joint_states", JointState, jointStatesCallback)

    # initialize JointCommands message
    command = AtlasCommand()

    # command.name = list(atlasJointNames)

    n = len(atlasJointNames)
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
        # initialPosition = initialPosition[16:23]
        initialPosition = array(currentJointState.position)

        # get joint commands from yaml
        y = traj_test[i]

        # first value is time duration
        dt = float(y[0])

        # subsequent values are desired joint positions
        commandPosition = array([ float(x) for x in y[1].split() ])

        # desired publish interval
        dtPublish = 0.02
        n = ceil(dt / dtPublish)

        for ratio in linspace(0, 1, n):
            command.k_effort[16:23] = [255] * 7
            interpCommand = (1 - ratio) * initialPosition + ratio * commandPosition
            command.position = [ float(x) for x in interpCommand ]
            # print command
            pub.publish(command)
            rospy.sleep(dt / float(n))
