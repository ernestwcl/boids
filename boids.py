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
%number of boids

boids_x=np.random.random_integers(-450.0,50.0,NBoids)
boids_y=np.random.random_integers(300.0,600.0,NBoids)
boid_x_velocities=np.random.random_integers(0,10.0,NBoids)
boid_y_velocities=np.random.random_integers(-20.0,20.0,NBoids)
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def too_close(xpos1,ypos1,xpos2,ypos2):
#True if boids become too close
	return (xpos1-xpos2)**2 + (ypos1-ypos2)**2 < 100
	
def same_flock(xpos1,ypos1,xpos2,ypos2):
#True if boids are close enough to be in the same flock
	return (xpos1-xpos2)**2 + (ypos1-ypos2)**2 < 10000)
	
def update_boids(boids):
	xpositions,ypositions,xvelocities,yvelocities=boids
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
			if too_close(xpositions[j],xpositions[i],ypositions[j],ypositions[i]):
				xvelocities[i]=xvelocities[i]+(xpositions[i]-xpositions[j])
				yvelocities[i]=yvelocities[i]+(ypositions[i]-ypositions[j])
	# Try to match speed with nearby boids
	for i in range(Nboids):
		for j in range(Nboids):
			if same_flock(xpositions[j],xpositions[i],ypositions[j],ypositions[i]):
				xvelocities[i]=xvelocities[i]+(xvelocities[j]-xvelocities[i])*FlockMatchSpeedWeight
				yvelocities[i]=yvelocities[i]+(yvelocities[j]-yvelocities[i])*FlockMatchSpeedWeight
	# Move according to velocities
	for i in range(Nboids):
		xpositions[i]=xpositions[i]+xvelocities[i]
		ypositions[i]=ypositions[i]+yvelocities[i]


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
