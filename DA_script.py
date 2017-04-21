import numpy as np


v = 2 # number of met variables
N = 6 # resolution of model grid
b=0.4 # probability to be on fire
mod_grid=N**2
x = np.random.choice([0, 1], size=mod_grid, p=[1-b, b])

def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """

    h, w = arr.shape
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))

def h_x_op(x):
    #x_MOD = x[0::2]  # these 4 lines mean MODIS and GEOSTAT are seperate state variables
    #x_geo = x[1::2]

    #x_MOD = x_MOD.reshape((N,N))
    #x_geo = x_geo.reshape((N,N))

    P_m = 2
    P_g = 3

    H_x_MOD = blockshaped(x,(P_m),(P_m))
    H_x_geo = blockshaped(x,(P_g),(P_g))

    H_x_MOD = np.sum(H_x_MOD,axis=(1,2))
    H_x_geo = np.sum(H_x_geo,axis=(1,2))

    print H_x_MOD,H_x_geo

h_x_op(x)

timesteps = 20
B = np.diag(np.ones(shape =mod_grid))
print B
