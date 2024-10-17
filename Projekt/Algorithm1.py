import numpy as np
import math
import librosa as lib

def compute_rms(x):
    sum = 0
    x_squared = np.square(x)
    sum = sum + np.sum(x_squared)
    return math.sqrt(sum/len(x))

def compute_snr(s,n):
    return 20 * math.log(compute_rms(s)/compute_rms(n),10)

def normalize(x, lvl):
    rms = compute_rms(x)
    scaling = math.pow(10, lvl/20) / rms

    return scaling * x

def trim(s,n):
    diff = len(n) - len(s)
    if(diff > 0):
        n = n[0: len(n) - diff ]
    else:
        s = s[0: len(s) - abs(diff) ]
    return s,n

def mix(s,n,k,lvl):
    s = s/max(abs(s))
    s = normalize(s, lvl)
    rms_s = compute_rms(s)
    n = n/max(abs(n))
    n = normalize(n, lvl)
    rms_n = compute_rms(n)
    p = (rms_s/math.pow(10, k/20))/rms_n
    noisy = s + p * n
    return noisy

def main():
    x = np.array([1,2,3,4])
    y = np.array([5,6,7,8,9])
    print(compute_rms(x))
    print(compute_snr(x,y))
    print(normalize(x,10))
    noise = lib.load("noise.wav")
    clean = lib.load("clean.wav")
    n,s = trim(noise, clean)


main()