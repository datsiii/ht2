import os

path = 'D:/projects/transfering_learning/images_folder/sources/Blagoveshchensky cathedral'
fds = sorted(os.listdir(path))

for img in fds:
    if img.endswith(('.1.jpg', '.png')):  # если имя оканчивается на что-то из tuple...
        print(img)  # выводим имя файла
        print(os.path.join(path, img))

#filelist = []
filelist = set()

path1 = 'D:/projects/transfering_learning/images_folder/sources'
for root, dirs, files in os.walk(path1):
    for file in files:
        # append the file name to the list
        filelist.add(os.path.join(root))

# print all the file names
for name in filelist:
    print(name)
    folderName = os.path.basename(name)
    print(folderName)
