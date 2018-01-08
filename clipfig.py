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

    # Remove illegal filename characters
    illegal = '\/:*?"<>|'
    for ill in illegal:
        filename = filename.replace(ill, '')

    # In case you're just trying to cause problems
    if filename == '':
        filename = 'Figure'

    picklefn = filename + pickleext
    imagefn = filename + imageext


    def numberfile(filename, number, zpad=4):
        # Put a _#### in the filename
        return '{:04}'.format(number).join(os.path.splitext(filename))

    # if file exists, start appending numbers
    if isfile(pjoin(outdir, picklefn)) or isfile(pjoin(outdir, imagefn)):
        # Need to escape square brackets, because they mean something in a glob pattern
        # replace the left square bracket with [[]
        glob_pattern = filename + '_*'
        glob_pattern = re.sub(r'\[', '[[]', glob_pattern)
        glob_pattern = re.sub(r'(?<!\[)\]', '[]]', glob_pattern)
        matches = fnmatch.filter(listdir(outdir), glob_pattern)
        if len(matches) == 0:
            # No matches, so it's the first repeated filename. rename it with _0002.
            picklefn = numberfile(picklefn, 2, zpad=4)
            imagefn = numberfile(imagefn, 2, zpad=4)
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
