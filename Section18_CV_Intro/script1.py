import cv2

impath = 'galaxy.jpg'

img = cv2.imread(impath, 0) # 1 is color, 0 is grayscale, -1 is color with alpha

print(img)
print(img.shape)
print(img.ndim)

resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow('Galaxy', resized_img)
cv2.imwrite('Galaxy_resized.jpg', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
