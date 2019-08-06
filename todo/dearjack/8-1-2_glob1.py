import os.path, glob
files = glob.glob("8-*.py")
for f in files: 
    print(os.path.abspath(f))