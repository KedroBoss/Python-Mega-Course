import cv2
import os

fpath = 'imgs'
rfpath = fpath + '/' + 'r_imgs'

imgs = []

for img_name in os.listdir(fpath):
    img = cv2.imread(os.path.join(fpath, img_name))
    if img is not None:
        resized_img = cv2.resize(img, (100,100))
        cv2.imwrite(rfpath+'/'+img_name+"100x100.jpg", resized_img)
