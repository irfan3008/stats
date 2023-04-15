import numpy as np
import pandas as pd

#define the data point

x = np.array([1,2,4,5,6,7,8,10])
y = np.array([2,4,6,7,9,11,12,14])

#calculate the mean of x and y

x_mean = np.mean(x)
y_mean = np.mean(y)

#calculate the term for numerator and denominator

n = (x - x_mean) * (y - y_mean)
d = ((x - x_mean) ** 2)

#calculate the beta and alpha

B = n / d
A1 = y_mean - (B * x_mean)

print(B)
print(A1)