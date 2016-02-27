from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import yaml



class BoidFlock(object):

		

	def __init__(self, config = 0): 

		#self.number = 50
		#self.lowlim = lowerposlimit = np.array([-450.0,300.0])
		#self.uplim = upperposlimit = np.array([50.0,600.0])
		#self.lowvlim = lowervellimit = np.array([0,-20.0])
		#self.upvlim = uppervellimit = np.array([10.0,20.0])
		if config == 0:
		
			self.number = 50
			self.lowlim = lowerposlimit = np.array([-450.0,300.0])
			self.uplim = upperposlimit = np.array([50.0,600.0])
			self.lowvlim = lowervellimit = np.array([0,-20.0])
			self.upvlim = uppervellimit = np.array([10.0,20.0])
		
		else:
			self.config = yaml.load(open(config))
			self.number = self.config['NUMBER_OF_BOIDS']
			self.lowlim  = np.array(self.config['LOWER_POS_LIM'])
			self.uplim = np.array(self.config['UPPER_POS_LIM'])
			self.lowvlim = np.array(self.config['LOWER_VEL_LIM'])
			self.upvlim = np.array(self.config['UPPER_VEL_LIM'])

		self.position = self.new_flock_positions()
		self.velocity = self.new_flock_velocities()
		

	def new_flock_positions(self):
		NBoids = self.number
		upper_limits = self.uplim
		lower_limits = self.lowlim
		range = upper_limits - lower_limits
		
		boidpositions  = lower_limits[:,np.newaxis] + np.random.rand(2, NBoids)*range[:,np.newaxis]
		
		return boidpositions
		#self.position = boidpositions
		
	def new_flock_velocities(self):
		NBoids = self.number
		upper_limits = self.upvlim
		lower_limits = self.lowvlim
		range = upper_limits - lower_limits
		
		boidvelocities = lower_limits[:,np.newaxis] + np.random.rand(2, NBoids)*range[:,np.newaxis]

		return boidvelocities
		#self.velocity = boidvelocities
		
	def set_position(self,position):
		self.position = position
		
	def set_velocity(self,velocity):
		self.velocity = velocity

		
	def update_positions(self):
		self.position = self.position + self.velocity
		
		
	def fly_to_middle(self):

		pos1 = self.position
		velo1 = self.velocity
		
		flockcenter = np.mean(pos1,1)
		direction_to_center = pos1 - flockcenter[:,np.newaxis]
		strength = 0.01
		velo1 -= (direction_to_center*strength)

		self.velocity=velo1
		
	def avoid_collisions(self):

		pos1 = self.position
		velo1 = self.velocity


		separations = pos1[:,np.newaxis,:] - pos1[:,:,np.newaxis]
		squared_diff = np.power(separations,2)
		squared_dist = np.sum(squared_diff,0)
		proximity_condition = 100
		not_too_close = squared_dist>=proximity_condition
		separations_if_too_close = np.copy(separations)
		separations_if_too_close[0,:,:][not_too_close]=0
		separations_if_too_close[1,:,:][not_too_close]=0
		
		velo1 += np.sum(separations_if_too_close,1)
		
		self.velocity=velo1
	
	def match_speed(self):

		xpos,ypos = self.position
		xvel,yvel = self.velocity
		# Try to match speed with nearby boids
		for i in range(len(xpos)):
			for j in range(len(xpos)):
				if (xpos[j]-xpos[i])**2 + (ypos[j]-ypos[i])**2 < 10000:


					xvel[i]=xvel[i]+(xvel[j]-xvel[i])*0.125/50
					yvel[i]=yvel[i]+(yvel[j]-yvel[i])*0.125/50

		
		
		self.velocity[0] = xvel
		self.velocity[1] = yvel
		
	def match_speed_modified(self):

		pos1 = self.position
		velo1 = self.velocity
	
		separations = pos1[:,np.newaxis,:] - pos1[:,:,np.newaxis]
		squared_diff = np.power(separations,2)
		squared_dist = np.sum(squared_diff,0)
		
		velocityseparation = velo1[:,np.newaxis,:] - velo1[:,:,np.newaxis]
		flock_size = 10000
		flock_formation_strength = 0.125
		outside_flock = squared_dist > flock_size
		
		velocityseparation_if_close = np.copy(velocityseparation)
		velocityseparation_if_close[0,:,:][outside_flock]=0
		velocityseparation_if_close[1,:,:][outside_flock]=0
		velo1 -= np.mean(velocityseparation_if_close,1)*flock_formation_strength
		self.velocity=velo1
		
	def update_velocities(self):
	
		#Fly toward the middle
		self.fly_to_middle()

		# Fly away from nearby boids
		self.avoid_collisions()
		
		# Match speed with flock
		self.match_speed()
		




	def update_boids(self):


		self.update_velocities()


		print repr(self.position[0])
		print repr(self.position[1])
		print repr(self.velocity[0])
		print repr(self.velocity[1])
		self.update_positions()
		print repr(self.position[0])
		print repr(self.position[1])
		print repr(self.velocity[0])
		print repr(self.velocity[1])

		
# boid = BoidFlock("config.yml")


# figure=plt.figure()
# axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
# scatter=axes.scatter(boid.position[0],boid.position[1])




# def animate(frame):

   # boid.update_boids()

   # scatter.set_offsets(boid.position.transpose())


# anim = animation.FuncAnimation(figure, animate,
                               # frames=50, interval=50)

# if __name__ == "__main__":
    # plt.show()
