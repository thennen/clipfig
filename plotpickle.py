# Load a pickled figure
import pickle
import sys
from matplotlib import pyplot as plt

fp = sys.argv[1]

with open(fp, 'rb') as f:
    pickle.load(f)

plt.show()
