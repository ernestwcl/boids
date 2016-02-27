from .. import boids as bf
from nose.tools import assert_almost_equal
import os
import yaml
import numpy as np

def test_bad_boids_update_boids():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/fixture.yml')))
    boid_data=regression_data["before"]
   
    positions  = np.append([np.asarray(boid_data[0])], [np.asarray(boid_data[1])], axis=0)
    velocities = np.append([np.asarray(boid_data[2])], [np.asarray(boid_data[3])], axis=0)
    
    boid = bf.BoidFlock("config.yml")
    boid.set_position(positions)
    boid.set_velocity(velocities)
    boid.update_boids()
    boid_data_after = np.append(boid.position, boid.velocity, axis=0) # boid data after update
	
    for after,before in zip(regression_data["after"],boid_data_after):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
	
def test_bad_boids_fly_middle():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/fixture_fly_middle.yml')))
    boid_data=regression_data["before"]
   
    positions  = np.append([np.asarray(boid_data[0])], [np.asarray(boid_data[1])], axis=0)
    velocities = np.append([np.asarray(boid_data[2])], [np.asarray(boid_data[3])], axis=0)
    
    boid = bf.BoidFlock("config.yml")
    boid.set_position(positions)
    boid.set_velocity(velocities)

    boid.fly_to_middle()
    boid_data_after = np.append(boid.position, boid.velocity, axis=0) # boid data after update
	
    for after,before in zip(regression_data["after"],boid_data_after):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
			
def test_bad_boids_avoid_collisions():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/fixture_avoid_collision.yml')))
    boid_data=regression_data["before"]
   
    positions  = np.append([np.asarray(boid_data[0])], [np.asarray(boid_data[1])], axis=0)
    velocities = np.append([np.asarray(boid_data[2])], [np.asarray(boid_data[3])], axis=0)
    
    boid = bf.BoidFlock("config.yml")
    boid.set_position(positions)
    boid.set_velocity(velocities)

    boid.avoid_collisions()
    boid_data_after = np.append(boid.position, boid.velocity, axis=0) # boid data after update
	
    for after,before in zip(regression_data["after"],boid_data_after):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
			
def test_bad_boids_match_speed():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/fixture_match_speed.yml')))
    boid_data=regression_data["before"]
   
    positions  = np.append([np.asarray(boid_data[0])], [np.asarray(boid_data[1])], axis=0)
    velocities = np.append([np.asarray(boid_data[2])], [np.asarray(boid_data[3])], axis=0)
    
    boid = bf.BoidFlock("config.yml")
    boid.set_position(positions)
    boid.set_velocity(velocities)

    boid.match_speed()
    boid_data_after = np.append(boid.position, boid.velocity, axis=0) # boid data after update
	
    for after,before in zip(regression_data["after"],boid_data_after):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
            
def test_bad_boids_update_velocities():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/fixture_update_velocities.yml')))
    boid_data=regression_data["before"]
   
    positions  = np.append([np.asarray(boid_data[0])], [np.asarray(boid_data[1])], axis=0)
    velocities = np.append([np.asarray(boid_data[2])], [np.asarray(boid_data[3])], axis=0)
    
    boid = bf.BoidFlock("config.yml")
    boid.set_position(positions)
    boid.set_velocity(velocities)

    boid.update_velocities()
    boid_data_after = np.append(boid.position, boid.velocity, axis=0) # boid data after update
	
    for after,before in zip(regression_data["after"],boid_data_after):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
			
def test_bad_boids_update_positions():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/fixture_update_positions.yml')))
    boid_data=regression_data["before"]
   
    positions  = np.append([np.asarray(boid_data[0])], [np.asarray(boid_data[1])], axis=0)
    velocities = np.append([np.asarray(boid_data[2])], [np.asarray(boid_data[3])], axis=0)
    
    boid = bf.BoidFlock("config.yml")
    boid.set_position(positions)
    boid.set_velocity(velocities)

    boid.update_positions()
    boid_data_after = np.append(boid.position, boid.velocity, axis=0) # boid data after update
	
    for after,before in zip(regression_data["after"],boid_data_after):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)