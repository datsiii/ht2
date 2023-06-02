'''import os

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
'''
import urllib.parse
import base64

with open('img.txt', 'r') as request:
    base64_img = request.read()
print(len(base64_img))
# Get image from POST request
#base64_img_bytes = base64_img.encode('utf-8')
with open('decoded_image.jpeg', 'wb') as file_to_save:
    # decoded_image_data = base64.decodebytes(base64_img_bytes)
    decoded_image_data = urllib.parse.unquote(base64_img)
    base64_img_bytes = decoded_image_data.encode('utf-8')
    decoded_image_data = base64.decodebytes(base64_img_bytes)
    file_to_save.write(decoded_image_data)
