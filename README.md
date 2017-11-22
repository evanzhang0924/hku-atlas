# HKU-Atlas


![Alt text](https://github.com/evanzhang0924/hku-atlas/raw/master/docs/intro1.jpg)
# 1. Introduction
>Human-machine interaction has been talked about for many years. Basically, we attached more importance to the interface between human and computer in the past several years. However, with the development of artificial intelligence and machine learning techniques, it is the time to focus on robotics field. In China, the Mi company has released a new kind of cleaning robot with high-technology automatic control system. It can sweep your house in quite a short time and with little noise. When we are impressed by such a smart home robot, it is interesting to note that this kind of robot is only sold no more than 2000 yuan, compared to other cleaning robot from Germany which has similar performance but values almost 6000 yuan. There is no doubt that high-tech company from China has already reached top level around the world.

>However, there is not so much research about the humanoid robot, especially relating to the humanoid biped robot. We all know that technology serves people,  so if the humanoid robot could be developed to a certain degree, we humans could be free from some repeating labor works. On one hand, there are some reasons to believe that one day the core technologies of humanoid robot has been studied further enough, we could make the humanoid robots exploit some particular terrain, such as in the abysmal sea, some nameless but dangerous cavern anyway. Moreover, imagine if there are some emergencies for example fire, our respective firefighters have to run into the scene of fire and rescuing victims, putting out the fire and saving valuable goods. However, we all know this kind of dangerous work has already killed so many firefighters. But I believe we could make some humanoid biped robots replacing those firefighters to do same work. It will not only save many lives of people, but also more efficient than normal human, because they are made by metal so that they are not afraid of the fire.

>On the other hand, we have seen so many Hollywood science fiction movies, the human-computer interactions perspective has been deeply boosted in those films. People are willing to pay money into the cinema because they agree with what those fiction movies show th them. A strong humanoid biped robot can do almost everything, like in the movie Real Steel. In the Disney park, there are also some humanoid robot standing here to interact with travellers. Those examples all show that humanoid biped robot is so attractive to our people, because they are made into human-like shape. Therefore, it seems that researching in the human-computer interactions with the humanoid biped robot is quite a meaningful task.

>In conclusion, in order to increase levels of both realism and human engagement, we want to be able to establish a physical connection between humanoid biped robot and normal participants. Throwing and catching objects from visitors to robots is one way of making such interaction, and of course we will maintain a safe distance. With this objective in mind, we are pleased to come up with that dissertation for human-robot physical interaction by ways of throwing and catching balls between a human and humanoid robot in the real world.

# 2. Analysis of the problem
>Our goal is always making the humanoid robot Atlas catch the ball, so we could simulate the entire process of ball catching by human to the Atlas. For ball catching with the Atlas, first of all, there should be a participant throwing the ball towards it. At the initial catch, it is better for the experiment to set the participant over against the humanoid robot, which could decrease the difficulty level and make it easier to catch it. As for the Atlas, it has to detect the ball, otherwise it is hard to imagine that catching a ball without the direction of the ball. During the ball flying in the air, the Atlas is computing the necessary information of it, and estimate the possible intersection points between the ball and the plane that the Atlas could reach. Before the ball arrives at the point, the Atlas should be ready to make a catching movement and of course earlier than the ball so as to catch the ball in its hand.

>in conclusion, the problem has been divided into three pieces:
>1. The Atlas has to identity the flying ball in the air which we called it ball detection problem.
>2. After identitying the ball, we have to make a estimation of ball trajectory. How to predict the ball tracking in a accurate enough level.
>3. And then, the Atlas needs to react so quickly that it ought to move its hand to the intersection point of ball trajectory and the plane that the Atlas could reach.





# 3. Curent Progress
>Have done about the ROS and DRCSIM tutorials

![Alt text](https://github.com/evanzhang0924/hku-atlas/raw/master/docs/ball throwing pic in gazebo.png)

>Have done the ball throwing in a fixed information such as velocity, time, angle, and so on towards the Atlas.

>Maybe it would be better if we know the detailed intersection coordination of the ball and the plane. In the Gazebo simulation, we could calculate to the data, but in the real world testing, we need a shooting machine of the tennis ball to set the initial velocity, acceleration and other data so that we know the landing position accurately.

>Working on the robot motion control part...


# 4. Reference
>[1] J. Kober, M. Glisson, and M. Mistry. Playing catch and juggling with a humanoid robot. In Proc. Int. Conf. on Humanoid Robots, 2012  

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

###### Wechat ID: zhangyp1114

###### Email Address: zhangyp2@hku.hk
