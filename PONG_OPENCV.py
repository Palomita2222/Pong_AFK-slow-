import cv2
import numpy as np
from PIL import ImageGrab as ig
import pyautogui as pgui
from time import sleep
import ctypes
User = ctypes.windll.user32
xVal = User.GetSystemMetrics(0)
yVal = User.GetSystemMetrics(1)

#READ 
ball = cv2.cvtColor(cv2.imread(r"C:\Users\rober\OneDrive\Escriptori\Code\Python\PONG\ball.png"), cv2.COLOR_BGR2GRAY)
sleep(5)

while True:
    pong_cam = ig.grab(bbox=(1130,440,1444,999))
    pong_cam = np.array(pong_cam)
    pong_cam = cv2.cvtColor(pong_cam, cv2.COLOR_RGB2GRAY)
    result_ball = cv2.matchTemplate(pong_cam, ball, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result_ball)
    x = ball.shape[0]
    y = ball.shape[1]
    if max_val > 0.8:
        pgui.moveTo(max_loc[0]+1130+y/2,max_loc[1]+440+y/2)
        cv2.rectangle(pong_cam, max_loc, (max_loc[0]+x, max_loc[1]+y), (0,255,0), 3)
    cv2.imshow("cam",pong_cam)
    cv2.imshow("result", result_ball)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
