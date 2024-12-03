import requests
import cv2
import numpy as np
import imutils

url = "http://127.0.0.1:5500/shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr =np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("Andoid_cam",img)

    if cv2.waitkey(1)==27:
        break
    cv2.destroyAllWindows()