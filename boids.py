"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random

# Deliberately terrible code for teaching purposes

NBoids = 50
#number of boids

FlockAttractionWeight = 0.01/NBoids
FlockMatchSpeedWeight = 0.125/NBoids
#flock behaviour weights

boids_x=np.random.random_integers(-450.0,50.0,NBoids)
boids_y=np.random.random_integers(300.0,600.0,NBoids)
boid_x_velocities=np.random.random_integers(0,10.0,NBoids)
boid_y_velocities=np.random.random_integers(-20.0,20.0,NBoids)
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

position_lower_limit = np.array([-450.0,300.0])
position_upper_limit = np.array([50.0,600.0])
velocity_lower_limit = np.array([0,-20.0])
velocity_upper_limit = np.array([10.0,20.0])

def new_flock_positions(number_boids, lower_limits, upper_limits):
	range = upper_limits - lower_limits
	
	boidpositions = lower_limits[:,np.newaxis] + np.random.rand(2, NBoids)*range[:,np.newaxis]

	return boidpositions
	
def new_flock_velocities(number_boids, lower_limits, upper_limits):
	range = upper_limits - lower_limits
	
	boidvelocities = lower_limits[:,np.newaxis] + np.random.rand(2, NBoids)*range[:,np.newaxis]

	return boidvelocities
	
	
def too_close(xpos1,xpos2,ypos1,ypos2):
#True if boids become too close
	return (xpos1-xpos2)**2 + (ypos1-ypos2)**2 < 100
	
def same_flock(xpos1,xpos2,ypos1,ypos2):
#True if boids are close enough to be in the same flock
	return (xpos1-xpos2)**2 + (ypos1-ypos2)**2 < 10000
	
def update_positions(xpos,ypos,xvel,yvel):
	for i in range(len(xpos)):
		xpos[i]=xpos[i]+xvel[i]
		ypos[i]=ypos[i]+yvel[i]
	return xpos, ypos
	
	
def fly_to_middle(pos1,velo1):

	
	flockcenter = np.mean(pos1,1)
	direction_to_center = pos1 - flockcenter[:,np.newaxis]
	strength = 0.01
	velo1 -= (direction_to_center*strength)

	return velo1
	
def avoid_collisions(pos1,velo1):

	separations = pos1[:,np.newaxis,:] - pos1[:,:,np.newaxis]
	squared_diff = np.power(separations,2)
	squared_dist = np.sum(squared_diff,0)
	proximity_condition = 100
	#boid_proximity = squared_dist < proximity_condition
	not_too_close = squared_dist>=proximity_condition
	separations_if_too_close = np.copy(separations)
	separations_if_too_close[0,:,:][not_too_close]=0
	separations_if_too_close[1,:,:][not_too_close]=0
	
	velo1 += np.sum(separations_if_too_close,1)
	return velo1
	
def update_velocities(boidpos,boidvel):
	#Fly toward the middle
	#for i in range(NBoids):
	#	for j in range(NBoids):
	#		xvel[i]=xvel[i]+(xpos[j]-xpos[i])*FlockAttractionWeight
	#		yvel[i]=yvel[i]+(ypos[j]-ypos[i])*FlockAttractionWeight

	boidvel = fly_to_middle(boidpos,boidvel)

	# Fly away from nearby boids
	#for i in range(NBoids):
	#	for j in range(NBoids):
	#		if too_close(xpos[j],xpos[i],ypos[j],ypos[i]):
#
#				xvel[i]=xvel[i]+(xpos[i]-xpos[j])
#				yvel[i]=yvel[i]+(ypos[i]-ypos[j])
	
	boidvel = avoid_collisions(boidpos,boidvel)
	
	xpos,ypos = boidpos
	xvel,yvel = boidvel
	# Try to match speed with nearby boids
	for i in range(NBoids):
		for j in range(NBoids):
			if same_flock(xpos[j],xpos[i],ypos[j],ypos[i]):


				xvel[i]=xvel[i]+(xvel[j]-xvel[i])*FlockMatchSpeedWeight
				yvel[i]=yvel[i]+(yvel[j]-yvel[i])*FlockMatchSpeedWeight
	
	return xvel,yvel

def update_boids(positions, velocities):
	xpositions,ypositions = positions
	xvelocities,yvelocities=boids = velocities

	velocities = update_velocities(positions,velocities)

	positions = update_positions(xpositions,ypositions,xvelocities,yvelocities)

		
positions = new_flock_positions(NBoids, position_lower_limit, position_upper_limit)
velocities = new_flock_velocities(NBoids, velocity_lower_limit, velocity_upper_limit)

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])



def animate(frame):

   update_boids(positions, velocities)

   scatter.set_offsets(positions.transpose())


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
