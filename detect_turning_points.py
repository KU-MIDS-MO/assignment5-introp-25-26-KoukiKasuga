import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    signal = np.asarray(signal)
    if signal.ndim != 1:
        raise ValueError("Input signal must be a 1D Numpy array.")
    
    diff = np.diff(signal) #discrete differences

    #detect sign change
    turning_indices = np.where(diff[:-1] * diff[1:] < 0)[0] + 1

    plt.figure()
    plt.plot(signal, label="Signal")
    plt.scatter(turning_indices, signal[turning_indices], color="red", label="Turning points")
    plt.title("Turning points in 'signal'")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()
    plt.tight_layout()

    plt.savefig(filename)
    plt.close

    return turning_indices
    pass