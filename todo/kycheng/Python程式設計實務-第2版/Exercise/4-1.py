#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'NCHC_PythonReading/todo/kycheng/Python程式設計實務-第2版/Exercise'))
	print(os.getcwd())
except:
	pass

#%%
import numpy as np 
import matplotlib.pyplot as plt 
x = np.arange(0,360)
y = np.sin(x*np.pi/180)
plt.plot(x, y)
plt.xlim(0,360)
plt.ylim(-1.2, 1.2)
plt.title("SIN Function")
plt.show()


#%%



