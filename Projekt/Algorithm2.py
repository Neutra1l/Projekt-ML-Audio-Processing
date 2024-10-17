import math

from Projekt import compute_rms

def compute_snr(s,n):
    return 20 * math.log(compute_rms(s)/compute_rms(n),10)

def main():
    arr = np.array([1,2,3,4])
    print(compute_snr(arr,3))

if __name__ == '__main__':
    main()