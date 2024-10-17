import numpy as np
import math

def compute_rms(x):
    sum = 0
    x_squared = np.square(x)
    sum = sum + np.sum(x_squared)
    return math.sqrt(sum/len(x))

def main():
    x = np.array([1,2,3,4])
    print(compute_rms(x))

if __name__ == '__main__':
    main()
