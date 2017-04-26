import os
import pickle
import fnmatch
from matplotlib import pyplot as plt

def clipboard_fig(fig):
    """
    Save fig as a png, a pickle, and copy both to the clipboard
    """

    pjoin = os.path.join
    isfile = os.path.isfile
    listdir = os.listdir
    splitext = os.path.splitext

    ax = fig.get_axes()[0]

    outdir = r'C:\t\plot_pickle\figures'
    pickleext = '.plt'
    imageext = '.png'

    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    # Try to come up with a title
    axtitle = ax.get_title().replace(' ', '_')
    xl = ax.get_xlabel().replace(' ', '_')
    yl = ax.get_ylabel().replace(' ', '_')
    if axtitle is not '':
        filename = axtitle
    elif yl is not '' and xl is not '':
        filename = '{}_vs_{}'.format(yl, xl)
    elif yl is not '':
        filename = yl
    elif xl is not '':
        filename = xl
    else:
        filename = 'Figure'

    picklefn = filename + pickleext
    imagefn = filename + imageext

    # if file exists, start appending numbers
    if isfile(pjoin(outdir, picklefn)) or isfile(pjoin(outdir, imagefn)):
        matches = fnmatch.filter(listdir(outdir), filename + '_*')
        if len(matches) == 0:
            picklefn = '_2'.join(splitext(picklefn))
            imagefn = '_2'.join(splitext(imagefn))
        else:
            # Get the string following the underscore
            numberstrings = [splitext(p)[0].replace(filename + '_', '') for p in matches]
            def wtf(string):
                try:
                    return int(string)
                except:
                    # if nothing after an underscore is a number, default to 2
                    return 2
            n = max(map(wtf, numberstrings))
            picklefn = '_{}'.format(n+1).join(splitext(picklefn))
            imagefn = '_{}'.format(n+1).join(splitext(imagefn))

    imagefp = pjoin(outdir, imagefn)
    picklefp = pjoin(outdir, picklefn)

    fig.savefig(imagefp )
    with open(picklefp , 'wb') as f:
        pickle.dump(fig, f)

    # Copy to clipboard with sweet C# program
    os.system('C:\\t\\plot_pickle\\file2clip \"{}\" \"{}\"'.format(picklefp, imagefp))

if __name__ == '__main__':
    clipboard_fig(plt.gcf())
