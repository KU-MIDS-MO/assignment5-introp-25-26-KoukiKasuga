import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    #ensure input is a 2D array
    if A.ndim != 2:
        raise ValueError("Input A must be a 2D Numpy array.")
    
    col_min = np.min(A, axis=0)
    col_max = np.max(A, axis=0)
    col_ranges = col_max - col_min

    fig = plt.figure()
    ax= fig.add_subplot(111)
    ax.bar(np.arange(A.shape[1]), col_ranges)
    plt.xlabel("Column index")
    plt.ylabel("Range of the column")
    plt.title("Column ranges")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

    return col_ranges
              
    pass