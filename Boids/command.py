
import sys
from argparse import ArgumentParser
from matplotlib import animation
from matplotlib import pyplot as plt
from boids import BoidFlock

# Command line entry point
def process():
    parser = ArgumentParser(description = "Flock of flying boids simulator")

    parser.add_argument('--file', '-f', dest = 'configFile')

    # Print help message even if no flag is provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
	

	# Catch exception if file does not exist
    try:
		# Create object
        boid = BoidFlock(args.configFile)
        # Plot figures
        figure = plt.figure()
        axes = plt.axes(xlim = (-500,1500), ylim = (-500,1500))
        scatter = axes.scatter(boid.position[0,:], boid.position[1,:])
        # Function handle for animate
        funcEval = lambda x: animate(boid, scatter)
        # Animate
        anim = animation.FuncAnimation(figure, funcEval, frames=50, interval=50)
        plt.show()
    except IOError:
        print "The file does not exist.\n" 
        parser.print_help()
    except:
        print "Unexpected error.\n"
		

def animate(boid, scatter):
	boid.update_boids()
	scatter.set_offsets(boid.position.transpose())

if __name__ == "__main__":
    process()