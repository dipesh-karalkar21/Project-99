import time
import os 
import shutil

path = "C:/Users/MAHESH KARALKAR/OneDrive/Desktop/Atharv/PythonCode/Project 99/i"
days = time.time()
print(days)
exist = os.path.exists(path)
print(exist)

if exist == True:
    ls = os.listdir(path)
    print(ls)
    for i in ls:
        newpath = os.path.join(path , i)
        print(newpath)
        data = os.stat(newpath)
        print(data)
        data_time = data.st_ctime
        print(data_time)
        if days <= data_time:
            if os.path.isfile(newpath) == True:
                os.remove(newpath)
            else:
                os.rmdir(newpath)
else:
    print("File Doesn't Exist")

