import os
sample_tree = os.walk("sampletree")
for dirname, subdir, files in sample_tree:
    for filename in files:
        print(os.path.abspath(filename))
    


    