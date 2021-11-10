#python
from __future__ import print_function
import time
from sr.robot import *

"""
run with:	$ python run.py exercise1.py
"""

R = Robot()
""" instance of the class Robot"""

a_th = 2.0

d_th = 0.4

def drive(speed, seconds):
    """
    Function for setting a linear velocity

    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

#here goes the code


def find_silver():
    """
    Function to find if a silver token is in range

    Returns:
	dist (float): distance to the silver token (-1 if no silver token is detected)
	rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
    """
    # We only look for the boxes nearby, i.e. which are at a distance of less than range = 1.5
    range = 1.5
    dist=range +1
	
    for token in R.see():
	# We only consider the silver boxes in the search area : dist<range but also that are in front of the robot (rot_y in [-90°;90°]) 
        if token.dist < min(range,dist) and -90<token.rot_y<90 and token.info.marker_type is MARKER_TOKEN_SILVER:
	    # If we found a closer silver boc, we update dist and rot_y with the value of this box
            dist = token.dist
            rot_y = token.rot_y
	
    # In case that we haven't found any box, we return negative value for dist because no real box is at a negative distance to the robot.
    if dist==range +1:
        return -1, -1
    else:
	# Otherwise, we return the caracteristics of the box
	return dist, rot_y

def orient():
    """ 
    If a silver marker is in range, turns the robot until it is aligned with it
    Returns :
    dist (float) : distance to the silver marker if in range, -1 otherwise
    """
    # To begin with, look for a silver bow in the nearby area using find_silver()
    dist, rot = find_silver()
    # If a silver box has been found (i.e. dist positive), we want to turn the robot towards it.
    if dist != -1 :
	# As long as the angle is outside a cetain interval, we turn the robot a little in the right direction
        while not (-a_th <rot< a_th):
            if rot<-a_th :
                turn(-5, 0.25)
            else:
                turn(+5, 0.25)
	    # We now update the value of the angle 
            junk, rot = find_silver()
		
    # Finally we return the distance to the silver box (or -1 if none was detected)      
    return dist

def obstacle(range, cone):
    """
    Check wether a golden token is on the path of the robot, looking between -cone
    and +cone degree within a certain range
    returns :
    rot (float) : angle between the robot and the closest obstacle
    """
    # initialisation of dist
    dist = range +1

    # We use the method see() of the robot class to get information on the environment
    for token in R.see():
	# We then only consider the golden boxes which are in the search area defined by range and cone.
	# We look for the closest one, and get its distance and angle to the robot. 
        if token.dist < min(range, dist) and -cone<token.rot_y<cone and token.info.marker_type is MARKER_TOKEN_GOLD:
            dist = token.dist
            rot = token.rot_y
		
    # If no obstacle was detected in the search area, we return a value which will not be taken otherwise
    if dist==range +1:
	    return 1000
    # If an obstacle was in fact detected, we return the angle between it and the robot
    else:
        return rot


def avoid(obs):
    """
    Given the direction in which to find the obstacle, the goal is to turn so that the obstacle is no longer an issue.
    Uses the input obs to determine which way to turn.
    Returns : angle with nearest obstacle after the manoeuvre to avoid obs.
    """

    #If the obstacle has been detected on the side of the robot, for precaution, we first go back a little to allow
    #It is to avoid having a robot too close to the sides of the golden token corridors
    if abs(obs)>15:
        drive(-20,0.4)

    #Then according to the sign of the angle obs, the robots turns one way or another
    if obs<0:
        turn(40, 0.17) 
    else:
        turn(-40, 0.17)

    #After the manoeuvre, we take a look at obstacles that are in front of the robot in a narrower field of view
    return obstacle(1.6, 15)



def corner(obs):
    """
    When the robot is stuck in a corner, the angle he makes with the nearest obstacle will change sign.
    At this point we can detect the corner and make a harder turn to escape in the right direction,
    which is in the opposite one from the last angle computed 

    Returns : angle with nearest obstacle after the manoeuvre to get out of the corner
    """    
    
    if obs<0:
        s=-1 
    else:
        s=1
    
    #if obs is small, tests concluded that the turn should last longer
    turn(-s*48, 0.90 + 0.015*(17-abs(obs)))

    #after the turn, we don't want to look too far in front of the robot
    #so that it may drive a little out of the corner even if it is not aligned properly
    return obstacle(0.9, 20)
    


def task():
    """ 
    Grabs the token and places it behind, then returns to position
    No inputs, no outputs
    """
    R.grab()
    turn(48,1.4)
    R.release()
    #after the release, the robot drives in reverse to avoid collision with the silver token
    drive(-20,1)
    #Then the robot goes back to his previous orientation
    turn(-48,1.4)



        
def main():

    time.sleep(1)

    #We give the robot a head start in the right direction
    drive(40, 6)
    
    #we then run an infinite loop
    while 1:

        #First we check wether silver tokens are present in the vicinity (at a distance inferior to 1.5)
        #If it's the case, we turn the robot until it is aligned with the token,
        #dist is then updated with the distance to the closest silver token
        #if no silver token is close, dist is equal to -1        
        dist = orient()

        #If the robot is close enough from the token, then it grabs it and place it behind him         
        if 0<=dist<d_th:
            task()

        else:
            #We then check if there are any obstacles in a range of 1.1 and for angles between -24 and +24 degrees
            #If there are, obs is updated with the angle to the closest obstacle
            #If no obstacle was detected, obs = 1000
            obs= obstacle(1.1, 24)
            
            #If there is an obstacle on the robot's way, we turn the robot until it is no longer the case
            #which means as long as obs !=1000
            while obs<1000:

                #for all actions, we keep track of the angle to the closest obstacle            
                previous = obs
                #Then we execute a manoeuvre to get away from the obstacle, and we get the new angle, after moving
                obs = avoid(obs)            
                
                #If the new angle and the old angle are of opposite signs, it means that the robot has found his way into a corner
                #in this case, we execute another type of manoeuvre, to get out
                if obs!=1000 and obs*previous<0:
                    obs = corner(obs)           

            
            
            #Now that our robot has been oriented into a direction avoiding obstacles, and if possible towards silver token,
            #we can move forward for a short amount of time 
            drive(35, 0.3) 
     


main()

