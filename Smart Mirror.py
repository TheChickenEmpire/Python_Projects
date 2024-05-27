import os
import cv2
import numpy as np
import datetime
import Important_stuff as Y
def Mirror(place):
    while True:
        cap = cv2.VideoCapture(0)
        h = ''
        g = 0
        status, photo = cap.read()
        try:
            while True:
                if g == 0:
                    try:
                        weather = Y.weather(place)
                        temp = Y.weather2(place)
                        humidity = Y.weather3(place) + '%'
                        temp = temp + ' Celsius'
                        if 'rain' in weather:
                            h = 'Bring unbrella'
                        g = 2
                    except TypeError:
                        print('Invalid place name')
                        break
                    except:
                        weather = 'ERROR'
                        temp = 'ERROR'
                        humidity = 'ERROR'
                else:
                    g = g - 0.00001
                today = datetime.datetime.today()
                today = today.strftime("%d/%m/%y")
                today2 = datetime.datetime.weekday(datetime.datetime.today())
                lis = 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'
                today2 = lis[today2]
                now = datetime.datetime.now()
                now = now.strftime("%H:%M:%S")
                status, photo = cap.read()
                cropped_frame = photo[200:400, 300:500]
                cropped_height, cropped_width, _ = cropped_frame.shape
                mask = np.zeros_like(photo)
                combined_frame = cv2.addWeighted(photo, 1, mask, 0.7, 0)
                combined_frame = cv2.flip(combined_frame, +1)
                combined_frame = cv2.putText(combined_frame, today+'                 '+temp,(10,465), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                combined_frame = cv2.putText(combined_frame, today2,(10,433), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                combined_frame = cv2.putText(combined_frame, '                         '+h,(10,433), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                combined_frame = cv2.putText(combined_frame, now+'            '+weather,(3,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                combined_frame = cv2.putText(combined_frame, '                    Humidity: '+humidity,(3,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                cv2.imshow("Smart Mirror", combined_frame)
                if cv2.waitKey(1) == 60:
                    pass
        except:
            print('RESTART Mirror Please')
            break
if __name__ == '__main__':
    t = input('Location:\n')
    Mirror(t)