import os

[filename, ext] = os.path.splitext('test.py')
print(filename + "va" + ext )