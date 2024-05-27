import requests 
import cv2 
import numpy as np 
import imutils
import time
import winsound
url = "http://192.168.1.20:8080/"
url = url + '/shot.jpg'
last_mean = 0
lf = 0
while True: 
    img_resp = requests.get(url) 
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
    img = cv2.imdecode(img_arr, -1) 
    img = imutils.resize(img, width=1000, height=1800) 
    if cv2.waitKey(1) == 27: 
        break
    cv2.imshow("Camera", img)
  
cv2.destroyAllWindows() 