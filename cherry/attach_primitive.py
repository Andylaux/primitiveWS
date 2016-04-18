#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from primitives.restOpen import RestOpenBehave
from primitives.pointArmLeft import PointArmLeftBehave
from primitives.question import QuestionBehave
from primitives.doubleMe import DoubleMeBehave
from primitives.swap import SwapBehave
from primitives.leftArmUp import LeftArmUpBehave
from primitives.hunkers import HunkersBehave
from primitives.led import Diode
from primitives.littleArmsUp import LittleArmsUpBehave

from primitives.idle import UpperBodyIdleMotion, HeadIdleMotion, TorsoIdleMotion

from textToSpeech.speak_3_old import Speak
from textToSpeech.say_text import SayText

from primitives.send_ip import SendIp

def attach_primitives(robot, isCamera=True):
    """ Attach all primitive to the robot.

    TO DO : Un parser pour faire automatiquement le nom afin de faire l'attachement seulement sur une boucle :
    for primitive in list_primitive:
        robot.attach_primitive(primitive(robot, 50), parser(primitive.name))

    Essayer aussi de se passer des imports ?
    """
    robot.attach_primitive(RestOpenBehave(robot),"rest_open_behave")
    robot.attach_primitive(PointArmLeftBehave(robot),"point_arm_left_behave")
    robot.attach_primitive(QuestionBehave(robot),"question_behave")
    robot.attach_primitive(DoubleMeBehave(robot),"double_me_behave")
    robot.attach_primitive(SwapBehave(robot),"swap_behave")
    robot.attach_primitive(LeftArmUpBehave(robot),"left_arm_up_behave")
    robot.attach_primitive(HunkersBehave(robot),"hunkers_behave")
    robot.attach_primitive(LittleArmsUpBehave(robot),"little_arms_up_behave")

    robot.attach_primitive(Diode(robot, 50),"diode_on")
    
    robot.attach_primitive(UpperBodyIdleMotion(robot, 50), 'upper_body_idle_motion')
    robot.attach_primitive(HeadIdleMotion(robot, 50), 'head_idle_motion')
    robot.attach_primitive(TorsoIdleMotion(robot, 50), 'torso_idle_motion')

    robot.attach_primitive(Speak(robot),"speak")
    robot.attach_primitive(SayText(robot),"say_text")

    robot.attach_primitive(SendIp(robot),"send_ip")
