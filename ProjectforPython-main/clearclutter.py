import os 

path = "D:\spare" #Path of my folder

x = os.listdir(path)
print(len(x))

for i in range(0,len(x)):
    new_name = str(i) + ".png"
    new_file_name = path + "\\" + new_name
    old_filepath_name = path + "\\" + x[i]
    os.rename(old_filepath_name,new_file_name)
    


