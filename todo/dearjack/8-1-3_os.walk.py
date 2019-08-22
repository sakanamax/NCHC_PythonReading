import os
sample_tree = os.walk("sampletree")
for dirname, subdir, files in sample_tree:
    print(dirname)
    print(subdir)
    print(files)
    print()