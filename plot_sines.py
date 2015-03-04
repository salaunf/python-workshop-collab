#!/usr/bin/env python

"""
    This script will plot a variable number of sine waves of increasingly
    doubled frequency as determined by input script arguments.  The plot
    will be rendered to the local matplotlib backend as well as optionally
    saved to a file, as determined by another input argument.
"""
import numpy as np

def construct_sines(n):
    """
        Construct the x axis and the sines depending on the
        integer number provided.

        Returns x, y numpy 1D arrays
    """
    x = np.linspace(0,2*np.pi,100)
    y = np.zeros(len(x))    
    for i in range(n):
        y += np.sin(2*i*x)
    y = np.array(y)/max(y)    
    return x,y



def plot_function(x, y, title=None,filename=None):
    """
        Plot the function based on the numpy arrays provided.

        If optional keyword argument filename is provided, save
        the figure there
    """   
    from matplotlib import pyplot as plt
    print
    print "Plot 1"
    
    if title == None:
        plt.title('Plot of X and Y')
    else:
        plt.title(str(title))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xticks
    
    plt.show()
    
    if title == None:    
        plt.savefig('default.png')
    else:
        plt.savefig(str(filename))
    
    pass


def main(options):
    """
        Main function to handle the input arguments and do the work
    """
    pass

if __name__ == '__main__':
    # Script arguments go here
    options = None

    main(options)
