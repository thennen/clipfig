# clipfig

This code does two things:

1. Gets matplotlib to plot pickled figures when you click on the file in windows.

2. Has a script that writes the current figure (png and pickle) to disk, and copies them both to the clipboard.

in action:
https://youtu.be/hEYoGQiDew0


You need to set up windows to recognize the pickled figure filetype (I used extension .plt).
The way I got this to work was using the registry keys in "make_plotting_work.bat".
You will need to change the file paths before adding to your registry.
Now when you click a .plt file, plotpickle.py will be run with the .plt file as an argument.

"clipfig.py" handles the figure clipping.  I found it useful to set the following macro in ipython:
%macro clip clipfig.py
Then when you just type "clip" in your console, clipfig.py writes a .png and .plt with non-conflicting filenames, and copies both of them to the clipboard using the small C# program file2clip.exe (source included)
