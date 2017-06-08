# Load a pickled figure
import pickle
import sys
from matplotlib import pyplot as plt

fp = sys.argv[1]

with open(fp, 'rb') as f:
    try:
        pickle.load(f)
    except:
        # Maybe it was pickled from python2 and you are running python3
        pickle.load(f, encoding='latin1')

plt.show()
