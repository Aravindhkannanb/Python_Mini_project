import cv2
from PIL import ImageGrab
import numpy as np
def capture():
    fourcc=cv2.VideoWriter_fourcc(*"XVID")
    out=cv2.VideoWriter("output.avi",fourcc,10,(1366,780))
    while True:
        img=ImageGrab.grab()
        img_np=np.array(img)
        frame=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
        cv2.imshow("screen Recorder",frame)
        out.write(frame)
        if cv2.waitKey(1)=='q':
            break
    out.release()
    cv2.destroyAllWindows()
capture()