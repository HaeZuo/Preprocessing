import os

path = "../images/total/"
folder_list = os.listdir(path)

print ("folder_list: {}".format(folder_list))

import shutil

folders=[
    'Folder',
]

for folder in folders:
    file_list = os.listdir(path+folder)
    count = 1
    for file in file_list:
        shutil.move(path+folder+"/"+file, path+folder+"/"+"{0:05d}".format(count)+".jpg")
        count += 1
