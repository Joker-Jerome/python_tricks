import matplotlib 
matplotlib.use('TkAgg') 
from matplotlib import pyplot
import numpy
import time
import multiprocessing
import sys
sys.stdout.flush()

start = time.time()

# initial conditions
size = 1000
num_processes = int(sys.argv[1])

y = multiprocessing.Array('d', 1000, lock=False)
new_y = multiprocessing.Array('d', 1000, lock=False)
y[480:520] = [1] * 40
new_y[480:520] = [1] * 40



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
def advance(dt, y, new_y, j):
    # diffusion via forward Euler
    sys.stdout.flush()
    new_y[j] += dt * (D * (y[j - 1] - 2 * y[j] + y[(j + 1) % size]))
    # reaction via forward Euler
    new_y[j] += dt * -y[j] * (1 - y[j]) * (alpha - y[j])
    return(new_y[j])

def update(dt, y, new_y, j):
    # diffusion via forward Euler
    y[j] = new_y[j]
    return(0)

# advance through t is at least 100; plot every 20
x_vec = list(range(1000))
process_pool = multiprocessing.Pool(num_processes, initializer=init_process, initargs=(y, new_y))
for t in numpy.arange(0, 100 + dt, dt):
    if t % 20 == 0:
        pyplot.plot(y, label='t = %g' % t)
    tmp = [process_pool.apply(advance, args = (dt, y, new_y, x,)) for x in x_vec]
    y[:] = new_y[:]


print('calculation: {} s'.format(time.time() - start))

pyplot.legend()
pyplot.show()