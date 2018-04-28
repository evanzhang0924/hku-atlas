# HKU-Atlas


![Alt text](https://github.com/evanzhang0924/hku-atlas/raw/master/docs/intro1.jpg)
# 1. Introduction
>Human-machine interaction has been talked for many years. Basically, we attached more importance to the interface between human and computer in the past several years. However, with the development of artificial intelligence and machine learning techniques, it is the time to focus on robotics field.

>However, there is not much research about the humanoid robot, especially relating to the humanoid biped one. On one hand, there are some reasons to believe that one day the core technologies of humanoid robot has been studied further enough, we could make the humanoid robots exploit some particular terrain, such as the abysmal sea area, some nameless but dangerous cavern and so on. On the other hand, we have seen so many Hollywood science fiction movies, the human-computer interactions has been deeply boosted in those films. People are willing to pay money into the cinema because they enjoy what those fiction movies show to them. Like in the movie Real Steel, a strong humanoid biped robot can do almost everything. Therefore, it seems that researching in the human-computer interactions with the humanoid biped robot is quite a meaningful topic.

>In conclusion, in order to increase levels of both realism and human engagement, I want to be able to establish a physical connection between humanoid biped robot and normal participants. Throwing and catching objects from visitors to robots is one way of making such interaction, and of course it will maintain a safe distance. With this objective in mind, I want to come up with that dissertation for human-robot physical interaction by ways of throwing and catching balls between a human and humanoid robot in the real world.

# 2. Analysis of the problem

![Alt text](https://github.com/evanzhang0924/hku-atlas/raw/master/docs/solution.png)

>In conclusion, the ball catching problem has been divided into three pieces:

>1. The Atlas has to identity the flying ball in the air which is ball detection. And it is better to track the ball contrail.

>2. After capturing the ball, a estimation of ball trajectory has been proposed. The output of this step will be passed into the last part.

>3. Finally, the Atlas moves its left arm to the corresponding position and catch the ball. A software MoveIt! could help to generate the trajectories. And ROS platform is to interact with Atlas robot.

# 3. Implementation
###### (1). System Flow Chart

![Alt text](https://github.com/evanzhang0924/hku-atlas/raw/master/docs/systemChart.png)

>As the figure shows, the camera will capture the tennis ball first which named ball detection. And then, the system will deal with the images and convert the ball information into the second part, trajectory estimation. At the beginning I tried to use a rough linear regression estimation, but it is not precise enough. Thus, it will turn into the nonlinear estimation for refinement. After reading many papers, I decided to use a parabolic model to describe that trajectory. Although it is not absolutely accurate, the outcome predicted would still reach the level. Next, the point predicted could be converted to the robot motion control part. After computation in the system, the Atlas will be controlled according to the motion planning outcome and its arm could be moved to the correct position before the ball arrives.

###### (2). The Gazebo World

![Alt text](https://github.com/evanzhang0924/hku-atlas/raw/master/docs/atlasCameraBall.png)

>Until now, the initial world configuration work has been finished. The Atlas robot, camera and ball are all at their correct position. Next, it is time to detect the ball through the camera and draw the path where ball passes.

###### (3). Ball Detection Algorithm Test

![Alt text](https://github.com/evanzhang0924/hku-atlas/raw/master/docs/ballCap.png)

>This figure shows that my ball detection algorithm is tested on a normal web camera called Logitech C525, and it has 8 MP and you can find it in many device stores. And this shows that the ball can be located and tracked under this algorithm which is really cool.

![Alt text](https://github.com/evanzhang0924/hku-atlas/raw/master/docs/balltest2.jpg)

>This figure shows that the ball detection algorithm is tested on a higher level industrial camera named GIGE, it is global shutter which could record the pixels simultaneously so that the tennis ball is captured very clearly.

###### (4). Experiment Result

![Alt text](https://github.com/evanzhang0924/hku-atlas/raw/master/docs/webcamera.png)

>This is a normal web camera Logitech C525, and initially I always test my algorithm in this hardware camera.

![Alt text](https://github.com/evanzhang0924/hku-atlas/raw/master/docs/industrialcamera.jpg)

>This is the higher level industrial camera GIGE, and at last time I test my algorithm in this camera and the outcome goes well too.

![Alt text](https://github.com/evanzhang0924/hku-atlas/raw/master/docs/ballCatch.png)

>As shown above, in Gazebo world, the ball has been catched by Atlas robot successfully.

![Alt text](https://github.com/evanzhang0924/hku-atlas/raw/master/docs/failcase.png)

>As shown above, sometimes the Atlas robot cannot catch the ball, for instance, the ball is thrown too high beyond the reachable range, or the ball is thrown in other directions. Under such situations, the Atlas will give a suitable animation for this, it just like saying "Sorry, I give up".

# 4. Reference
>[1] J. Kober, M. Glisson, and M. Mistry. Playing catch and juggling with a humanoid robot. In Proc. Int. Conf. on Humanoid Robots, 2012.  

>[2] E. J. Carter, M. N. Mistr, and G. Peter K. Carr. Playing Catch with Robots: Incorporating Social Gestures into Physical Interactions.

>[3] M. Riley and C.G. Atkeson, “Robot Catching: Towards Engaging Human-Humanoid Interaction, ” Autonomous Robots, vol. 12, no. 1, pp. 119-128, Jan. 2002.

>[4] K. Deguchi, H. Sakurai, and S. Ushida, “A goal oriented just-in-time visual servoing for ball catching robot arm, ” in Proc. Int. Conf. on Intelligent Robots and Systems, 2008.

>[5] R. Mori and F. Miyazaki, “Examination of human ball catching strategy though autonomous mobile robot, ” in IEEE International Conference on Robotics and Automation, pp. 4236-4241, 2002.

>[6] V. Lippiello and F. Ruggiero, “Monocular eye-in-hand robotic ball catching with parabolic motion estimation, ” in 10th International IFAC Symposium on Robot Control, pp. 229-234, 2012.

>[7] S. Chapman, “Catching a Baseball”, American Journal of Physics, vol.36, pp. 868-870, 1968.

>[8] B. Bauml, T. Wimbock, and G. Hirzinger, “Kinematically optimal catching a flying ball with a hand-arm-system, ” in Proc. Int. Conf. on Intelligent Robots and Systems, 2010.

>[9] V. Lippiello, F. Ruggiero, B. Siciliano, and L. Villani, “Visual grasp planning for unknown objects using a multifingered robotic hand, ” IEEE/ASME Transactions on Mechatronics, vol. pp. 1050-1059, 2013.

>[10] S. Kim, A. Shukla, and A. Billard, “Catching objects in flight, ” IEEE Transactions on Robotics, 2014.

# 5. Contact information

###### Phone Number: 67658229

###### Email Address: zhangyp2@connect.hku.hk
