import cv2, time

video=cv2.VideoCapture(0)#Number is camera

a=0
while True:
    a+=1
    check, frame = video.read()

    #time.sleep(3)

    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Img', gray_img)

    #res_img=cv2.resize(video, (int(video.shape[1]/2),int(video.shape[0]/2)))
    key=cv2.waitKey(1)
    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows()
print(a)
