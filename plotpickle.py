# Load a pickled figure
import pickle
import sys
from matplotlib import pyplot as plt

plt.ion()

fp = sys.argv[1]

with open(fp, 'rb') as f:
    try:
        fig = pickle.load(f)
    except:
        # Maybe it was pickled from python2 and you are running python3
        fig = pickle.load(f, encoding='latin1')
    finally:
        axs = fig.get_axes()
        ax = axs[0]

print('Figure loaded.  Variables \'fig\' and \'ax\' defined.')
plt.show()
