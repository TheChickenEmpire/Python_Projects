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
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = np.abs(np.mean(gray) - last_mean)
    print(result)
    if result > 100:
        pass
    elif result > 0.99:
        print('Motion Detected!')
        print(result)
        lf = int(lf)
        lf = lf + 1
        lf = str(lf)
        file = "C:\\Users\\lucas\\OneDrive\\Python_Projects\\Security Camera\\"+lf+".jpg"
        cv2.imwrite(file, img)
        duration = 1000
        freq = 440
        winsound.Beep(freq, duration)
        time.sleep(0.5)
    last_mean= np.mean(gray)
    if cv2.waitKey(1) == 27: 
        break
    cv2.imshow("Camera", img)
  
cv2.destroyAllWindows() 