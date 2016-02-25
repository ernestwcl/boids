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
	
def update_boids(positions, velocities):
	xpositions,ypositions = positions
	xvelocities,yvelocities=boids = velocities
	Nboids = len(xpositions)
	FlockAttractionWeight = 0.01/NBoids
	FlockMatchSpeedWeight = 0.125/Nboids
	# Fly towards the middle
	
	for i in range(Nboids):
		for j in range(Nboids):
			xvelocities[i]=xvelocities[i]+(xpositions[j]-xpositions[i])*FlockAttractionWeight
			yvelocities[i]=yvelocities[i]+(ypositions[j]-ypositions[i])*FlockAttractionWeight
	# Fly away from nearby boids
	for i in range(Nboids):
		for j in range(Nboids):
			#if (xpositions[j]-xpositions[i])**2 + (ypositions[j]-ypositions[i])**2 <100:
			if too_close(xpositions[j],xpositions[i],ypositions[j],ypositions[i]):

				xvelocities[i]=xvelocities[i]+(xpositions[i]-xpositions[j])
				yvelocities[i]=yvelocities[i]+(ypositions[i]-ypositions[j])
	# Try to match speed with nearby boids
	for i in range(Nboids):
		for j in range(Nboids):
			if same_flock(xpositions[j],xpositions[i],ypositions[j],ypositions[i]):
			#if (xpositions[j]-xpositions[i])**2 + (ypositions[j]-ypositions[i])**2 <100:

				xvelocities[i]=xvelocities[i]+(xvelocities[j]-xvelocities[i])*FlockMatchSpeedWeight
				yvelocities[i]=yvelocities[i]+(yvelocities[j]-yvelocities[i])*FlockMatchSpeedWeight
	# Move according to velocities
	#for i in range(Nboids):
	#	xpositions[i]=xpositions[i]+xvelocities[i]
	#	ypositions[i]=ypositions[i]+yvelocities[i]
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
