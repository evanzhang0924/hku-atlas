#!/usr/bin/env python

# Author: ZHANG Yupeng

# First of all, to use the python interface to the Boston Dynamics
# Humanoid Atlas Robot, it has to import some related packages, such
# as moveit_commander module, rospy and messaes and so on that I will
# use laterly.

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

# And the messages notice has to be imported as well..
from std_msgs.msg import String

atlasJointNames = [
  'atlas::back_lbz', 'atlas::back_mby', 'atlas::back_ubx', 'atlas::neck_ay',
  'atlas::l_leg_uhz', 'atlas::l_leg_mhx', 'atlas::l_leg_lhy', 'atlas::l_leg_kny', 'atlas::l_leg_uay', 'atlas::l_leg_lax',
  'atlas::r_leg_uhz', 'atlas::r_leg_mhx', 'atlas::r_leg_lhy', 'atlas::r_leg_kny', 'atlas::r_leg_uay', 'atlas::r_leg_lax',
  'atlas::l_arm_usy', 'atlas::l_arm_shx', 'atlas::l_arm_ely', 'atlas::l_arm_elx', 'atlas::l_arm_uwy', 'atlas::l_arm_mwx',
  'atlas::r_arm_usy', 'atlas::r_arm_shx', 'atlas::r_arm_ely', 'atlas::r_arm_elx', 'atlas::r_arm_uwy', 'atlas::r_arm_mwx']


currentJointState = JointState()


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
    print plan1


    print "============= Waiting while RVIZ displays plan1..."
    rospy.sleep(5)


    # Asking RVIZ to visualize the trajectory for me, although the group.plan()
    # method does this work automatically so this is not that meaningful and it
    # just displays the same trajectory again.
    # print "============= Visualize plan1"
    # display_trajectory_again = moveit_msgs.msg.DisplayTrajectory()
    #
    # display_trajectory_again.trajectory_start = robot.get_current_state()
    # display_trajectory_again.append(plan1)
    # display_trajectory_publisher.publish(display_trajectory_again)
    #
    # print "============= Waiting wile plan1 is visualized again."
    # rospy.sleep(5)


    # Moving to a pose goal
    # group.go(wait=True)

    # group.execute(plan1)

    ## Planning to a joint-space goal
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ##
    ## Let's set a joint space goal and move towards it.
    ## First, we will clear the pose target we had just set.

    # group.clear_pose_targets()
    #
    # ## Then, we will get the current set of joint values for the group
    # group_variable_values = group.get_current_joint_values()
    # print "============ Joint values: ", group_variable_values
    #
    # ## Now, let's modify one of the joints, plan to the new joint
    # ## space goal and visualize the plan
    # group_variable_values[0] = 1.0
    # group.set_joint_value_target(group_variable_values)
    #
    # plan2 = group.plan()
    #
    # print "============ Waiting while RVIZ displays plan2..."
    # rospy.sleep(5)
    #
    #
    # ## Cartesian Paths
    # ## ^^^^^^^^^^^^^^^
    # ## You can plan a cartesian path directly by specifying a list of waypoints
    # ## for the end-effector to go through.
    # waypoints = []
    #
    # # start with the current pose
    # waypoints.append(group.get_current_pose().pose)
    #
    # # first orient gripper and move forward (+x)
    # wpose = geometry_msgs.msg.Pose()
    # wpose.orientation.w = 1.0
    # wpose.position.x = waypoints[0].position.x + 0.1
    # wpose.position.y = waypoints[0].position.y
    # wpose.position.z = waypoints[0].position.z
    # waypoints.append(copy.deepcopy(wpose))
    #
    # # second move down
    # wpose.position.z -= 0.10
    # waypoints.append(copy.deepcopy(wpose))
    #
    # # third move to the side
    # wpose.position.y += 0.05
    # waypoints.append(copy.deepcopy(wpose))
    #
    # ## We want the cartesian path to be interpolated at a resolution of 1 cm
    # ## which is why we will specify 0.01 as the eef_step in cartesian
    # ## translation.  We will specify the jump threshold as 0.0, effectively
    # ## disabling it.
    # (plan3, fraction) = group.compute_cartesian_path(
    #                              waypoints,   # waypoints to follow
    #                              0.01,        # eef_step
    #                              0.0)         # jump_threshold
    #
    # print "============ Waiting while RVIZ displays plan3..."
    # rospy.sleep(5)
    #
    # # Uncomment the line below to execute this plan on a real robot.
    # # group.execute(plan3)
    #
    #
    # ## Adding/Removing Objects and Attaching/Detaching Objects
    # ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # ## First, we will define the collision object message
    # collision_object = moveit_msgs.msg.CollisionObject()
    #
    #
    #
    # ## When finished shut down moveit_commander.
    # moveit_commander.roscpp_shutdown()

    ## END_TUTORIAL

    print "============ STOPPING"

def jointStatesCallback(msg):
    global currentJointState
    currentJointState = msg



if __name__ == "__main__":
    try:
        atlas_move_python()
    except rospy.ROSInterruptException:
        pass

    # First of all, it is important to check that the input arguments are correct
    # if len(sys.argv) != 3:
    #     print "usage: traj_moveit_control.py YAML_FILE TRAJECTORY_NAME"
    #     print "     where TRAJECTORY is a dictionary defined in YAML_FILE"
    #     sys.exit(1)
    # traj_yaml = yaml.load(file(sys.argv[1], 'r'))
    traj_yaml = values
    # traj_name
    # if not traj_name in traj_yaml:
    #     print "unable to find trajectory %s in %s" % (traj_name, sys.argv[1])
    #     sys.exit(1)
    # traj_len = len(traj_yaml[traj_name])
    traj_len = 36

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
        y = values[i]

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
