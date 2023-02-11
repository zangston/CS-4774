# import necessary libraries

import numpy
import matplotlib.pyplot as plt

# better safe than sorry....
# print("environment test")

# define identity matrix as specified in Case I according to assignment description
matrix_identity = numpy.identity(2)

# define diagonal matrix
matrix_diagonal = numpy.diag([2, 4])

# define number of samples taken
sample_size = 500

# generate samples from distributions using each covariance matrix
samples_cm_identity = numpy.random.multivariate_normal([0, 0], matrix_identity, sample_size)
samples_cm_diagonal = numpy.random.multivariate_normal([0, 0], matrix_diagonal, sample_size)

# plot generated samples
plt.scatter(samples_cm_identity[:, 0], samples_cm_identity[:, 1], color='teal',
            label='Samples generated with Identity matrix')
plt.scatter(samples_cm_diagonal[:, 0], samples_cm_diagonal[:, 1], color='pink',
            label='Samples generated with Diagonal matrix')
