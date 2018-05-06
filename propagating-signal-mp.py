import matplotlib 
#matplotlib.use('TkAgg')  
from matplotlib import pyplot
import numpy
import time
import multiprocessing
import sys

start = time.time()

# initial conditions
size = 1000
num_processes = int(sys.argv[1])



# parameters
D = 20         # diffusion constant/dx^2
alpha = 0.3    # threshold

# time-step
dt = 0.01


def init_process(y_to_share, new_y_to_share): 
    global y, new_y
    y = y_to_share
    new_y = new_y_to_share
    

# our rule for reaction-diffusion
def advance(j):
    # diffusion via forward Euler
    new_y[j] += dt * (D * (y[j - 1] - 2 * y[j] + y[(j + 1) % size]))
    #print("-"*20)
    # reaction via forward Euler
    new_y[j] += dt * -y[j] * (1 - y[j]) * (alpha - y[j])
    #print(y[:])
    #print(new_y[:])
    #print(new_y[j])
    return(new_y[j])

# update
def update(j):
    y[j] = new_y[j]
    #return(new_y[j])

# initialize the share array

y_l = multiprocessing.Array('d', 1000, lock=False)
new_y_l = multiprocessing.Array('d', 1000, lock=False)
y_l[480:520] = [1] * 40
new_y_l[480:520] = [1] * 40
#y = y_l
#new_y = y[:]

# advance through t is at least 100; plot every 20
x_vec = list(range(1000))
process_pool = multiprocessing.Pool(num_processes, initializer=init_process, initargs=(y_l, new_y_l))
for t in numpy.arange(0, 100 + dt, dt):
    y_tmp = process_pool.map(advance, x_vec)
    process_pool.map(update, x_vec)
    #print("y_l")
    #print(y_tmp[:])
    if t % 20 == 0:
        pyplot.plot(y_tmp, label='t = %g' % t)

print('calculation: {} s'.format(time.time() - start))

pyplot.legend()
pyplot.show()
