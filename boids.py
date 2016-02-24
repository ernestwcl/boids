"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

NBoids = 50
%number of boids

boids_x=[random.uniform(-450,50.0) for x in range(NBoids)]
boids_y=[random.uniform(300.0,600.0) for x in range(NBoids)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(NBoids)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(NBoids)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def Too_close(xpos1,ypos1,xpos2,ypos2):
	return (xpos1-xpos2)**2 + (ypos1-ypos2)**2 < 100

def update_boids(boids):
	xpositions,ypositions,xvelocities,yvelocities=boids
	# Fly towards the middle
	Nboids = len(xpositions)
	for i in range(Nboids):
		for j in range(Nboids):
			xvelocities[i]=xvelocities[i]+(xpositions[j]-xpositions[i])*0.01/Nboids
	for i in range(Nboids):
		for j in range(Nboids):
			yvelocities[i]=yvelocities[i]+(ypositions[j]-ypositions[i])*0.01/Nboids
	# Fly away from nearby boids
	for i in range(Nboids):
		for j in range(Nboids):
			if Too_close(xpositions[j],xpositions[i],ypositions[j],ypositions[i]):
				xvelocities[i]=xvelocities[i]+(xpositions[i]-xpositions[j])
				yvelocities[i]=yvelocities[i]+(ypositions[i]-ypositions[j])
	# Try to match speed with nearby boids
	for i in range(Nboids):
		for j in range(Nboids):
			if (xpositions[j]-xpositions[i])**2 + (ypositions[j]-ypositions[i])**2 < 10000:
				xvelocities[i]=xvelocities[i]+(xvelocities[j]-xvelocities[i])*0.125/Nboids
				yvelocities[i]=yvelocities[i]+(yvelocities[j]-yvelocities[i])*0.125/Nboids
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
