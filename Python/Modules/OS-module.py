import os
print(os.getcwd()) ## Current working directory
print(os.listdir())
os.chdir(r"/")# changes the particular directory
print(os.getcwd())
os.mkdir(r"/\Python\Modules\Modulesss") ## create new directory
os.rmdir(r"/\Python\Modules\Modulesss") ## remove the directory
print(os.getpid()) # to get the current working process ID
print(os.getppid()) # to get the parent process ID

