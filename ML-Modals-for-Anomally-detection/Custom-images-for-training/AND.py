import cv2 as cv
import os

cwd = os.getcwd()

lis = [0,1,'D']
pathLis = []
for i in lis:
    pathLis.append(os.path.join(cwd,f'{i}'))
for fol in pathLis:
    if not os.path.exists(fol):
        os.mkdir(fol)
frames = os.path.join(cwd,'Frames')
lis = os.listdir(frames)
winname = 'frames'
for item in lis:
    cv.namedWindow(winname,cv.WINDOW_NORMAL)
    path = os.path.join(frames,item)
    img = cv.imread(path)
    cv.imshow(winname,img)
    while True:
        key = cv.waitKey(0)
        if key == ord('a'):
            print(f"Accirdnt,{item}")
            save = os.path.join(pathLis[0],item)
            cv.imwrite(save,img)

        elif key == ord('n'):
            print(f"NoAccirdnt,{item}")
            save = os.path.join(pathLis[1],item)
            cv.imwrite(save,img)

        elif key == ord('d'):
            print(f"NoAccirdnt,{item}")
            save = os.path.join(pathLis[2],item)
            cv.imwrite(save,img)
            break

        elif key == ord('q'):
            exit(0)

        else:
            print('Invalid Input')
            continue
        os.remove(path)
        break

