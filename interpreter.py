#---DEPENDENCIES--------------------------------------------------------------+
import numpy as np
from keyboard import is_pressed
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
import cv2,time
from sysControls import decide_task

#---GESTURES------------------------------------------------------------------+
s_ = [0,0,0,0,0,0,0,1]
g1 = [0,0,0,0,0,0,1,0]
g2 = [0,0,0,0,0,1,0,0]
g3 = [0,0,0,0,1,0,0,0]
g4 = [0,0,0,1,0,0,0,0]
g5 = [0,0,1,0,0,0,0,0]
g6 = [0,1,0,0,0,0,0,0]
_s = [1,0,0,0,0,0,0,0]

#---LANGUAGES-----------------------------------------------------------------+
language={
    'c1':[7,6,0],
    'c2':[7,5,0],
    'c3':[7,4,0],
    'c4':[7,3,0],
    'c5':[7,2,0],
    'c6':[7,1,0],
    'c7':[7,6,5,0],
    'c8':[7,5,4,0],
    'c9':[7,4,3,0],
    'c10':[7,3,2,0],
    'c11':[7,2,1,0],
    'c12':[7,1,6,0]

}

def cnvt_gesture(gest):
  return gest.index(max(gest))

def get_key(val):
    for key, value in language.items():
         if val == value:
             return key

#---MODEL---------------------------------------------------------------------+
model = 'M1.h5'
GCF = keras.models.load_model(f'{model}')   # CNN used for GCF

#---PARSER--------------------------------------------------------------------+
def collect_gesture():

    cam = cv2.VideoCapture(0)
    time.sleep(3)  # time before starting camera

    snap = 60      # shutter waiting time
    wait = 0       # count
    seq=[]
    print('press q to quit:')
    while True:
        
        if wait == snap: # captures image only when wait = snap
            
            ret, frame = cam.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame, (64,64), interpolation = cv2.INTER_AREA)
            
            if ret:
                arr = np.array(frame)
                arr = arr.reshape((1,64,64,1))
                pred = GCF.predict(arr)
                print(pred)
                pred=list(pred[0])

                if pred==s_:
                  seq.append(7)
                
                if len(seq):
                  if pred.index(1)==seq[-1]:
                    continue
                  elif pred!=_s:
                    seq.append(pred.index(1))
                  else:
                    seq.append(0)
                    decide_task(language(get_key(seq)))
                    seq=[]
            else:
                break
            wait = 0
        else:
            wait += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        if is_pressed('q'):
          break

    cam.release()
    cv2.destroyAllWindows()
if __name__=='__main__':
  collect_gesture()
    