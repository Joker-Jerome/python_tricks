import time

N = 10000
aa = np.arange(-N,N)

#%timeit np.searchsorted(aa, N/2)+1
#%timeit np.argmax(aa>N/2)
#%timeit np.where(aa>N/2)[0][0]
#%timeit np.nonzero(aa>N/2)[0][0]
