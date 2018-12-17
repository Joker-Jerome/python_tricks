# import 
import h5py

# basic operations
f = h5py.File('mytestfile.hdf5', 'r')
list(f.keys())
dset = f['mydataset']
dset.shape
dset.dtype

# create a file
dset = f.create_dataset("mydataset", (100,), dtype='i')


