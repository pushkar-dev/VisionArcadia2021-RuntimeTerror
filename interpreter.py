#---DEPENDENCIES--------------------------------------------------------------+
import numpy as np
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
    'c1':[7,6,_s],
    'c2':[7,g2,_s],
    'c3':[7,g3,_s],
    'c4':[7,g4,_s],
    'c5':[7,g5,_s],
    'c6':[7,g6,_s],
    'c7':[7,6,g2,_s],
    'c8':[7,g2,g3,_s],
    'c9':[7,g3,g4,_s],
    'c10':[7,g4,g5,_s],
    'c11':[7,g5,g6,_s],
    'c12':[7,g6,6,_s],

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
    while True:
        
        if wait == snap: # captures image only when wait = snap
            
            ret, frame = cam.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame, (64,64), interpolation = cv2.INTER_AREA)
            
            if ret:
                arr = np.array(frame)
                arr = arr.reshape((1,64,64,1))
                pred = GCF.predict(arr)
                pred=list(pred)

                if pred==s_:
                  seq.append(s_)
                
                if len(seq):
                  if pred==seq[-1]:
                    continue
                  elif pred!=_s:
                    seq.append(pred)
                  else:
                    seq.append(pred)
                    decide_task(language(get_key(seq)))
                    seq=[]
            else:
                break
            wait = 0
        else:
            wait += 1
            
        #Break if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cam.release()
    cv2.destroyAllWindows()
if __name__=='__main__':
  collect_gesture()
    