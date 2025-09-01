import cv2 as cv
import os

cwd = os.getcwd()
lis = os.listdir(cwd)
output_folder = os.path.join(cwd,'Frames')
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
i = 0
print(lis)
# exit(0)
for item in lis:
    path = os.path.join(cwd,item)
    if not os.path.isfile(path):
        continue
    if item.split('.')[-1] != 'mpg':
        continue
    print('\n',item)
    vid = cv.VideoCapture(path)
    if not vid.isOpened():
        continue
    fps = vid.get(cv.CAP_PROP_FPS)
    frame_num = 0
    print(f"fps={fps}")
    fps = 15
    while True:
        mod = int(fps/2)
        ret, image = vid.read()
        if not ret:
            break
        if frame_num % mod == 0:
            fp = os.path.join(output_folder, f'{i}.jpg')
            cv.imwrite(filename=fp,img=image)
            i+=1
            print(i,', ',end='')
        frame_num+=1
