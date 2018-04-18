from matplotlib import pyplot
import numpy
import time
import itertools
from mpi4py import MPI

start = time.time()

# initial conditions
size = 1000
idx_vec = 1:1000

# mpi 
communicator = MPI.COMM_WORLD
rank = communicator.rank
nnode = communicator.size

num_each = size // nnode

start = num_each * rank
stop = num_each * (rank + 1)
if rank == nnode - 1: stop = size

y = [0] * size
y[480:520] = [1] * 40

# parameters
D = 20         # diffusion constant/dx^2
alpha = 0.3    # threshold

# time-step
dt = 0.01


# our rule for reaction-diffusion
def advance(dt, y):
    new_y = list(y)
    for j in range(start, stop):
        # diffusion via forward Euler
        new_y[j] += dt * (D * (y[j - 1] - 2 * y[j] + y[(j + 1) % size]))

        # reaction via forward Euler
        new_y[j] += dt * -y[j] * (1 - y[j]) * (alpha - y[j])

    return new_y

# advance through t is at least 100; plot every 20
for t in numpy.arange(0, 100 + dt, dt):
    if t % 20 == 0:
        if not rank:
            pyplot.plot(y, label='t = %g' % t)
    y = advance(dt, y)
    y = list(itertools.chain.from_iterable(communicator.allgather(y[start:stop]))
if not rank:
    print('calculation: {} s'.format(time.time() - start_time))

    pyplot.legend()
    pyplot.show()