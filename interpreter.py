#---DEPENDENCIES--------------------------------------------------------------+
import numpy as np
from keyboard import is_pressed
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow import keras
import cv2,time
from sysControls import decide_task

#---GESTURES------------------------------------------------------------------+
# >>> indices
# s_ = 8
# g1 = 1
# g2 = 2
# g3 = 3
# g4 = 4
# g5 = 5
# g6 = 6
# na = 7
# _s = 0
# <<<

#---LANGUAGES-----------------------------------------------------------------+
language = {
    'c1':[8,6,0],
    'c2':[8,5,0],
    'c3':[8,4,0],
    'c4':[8,3,0],
    'c5':[8,2,0],
    'c6':[8,1,0],
    'c7':[8,6,5,0],
    'c8':[8,5,4,0],
    'c9':[8,4,3,0],
    'c10':[8,3,2,0],
    'c11':[8,2,1,0],
    'c12':[8,1,6,0]}

def cnvt_gesture(gest):
    return gest.index(max(gest))

def get_key(val):
    for key, value in language.items():
         if val == value:
             return key
    else: return None

#---MODEL---------------------------------------------------------------------+
model = 'M1.h5'
GCF = keras.models.load_model(f'models/{model}')   # CNN used for GCF

img_size = GCF.input_shape[1:3]

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
            frame = cv2.resize(frame,img_size,interpolation = cv2.INTER_AREA)
            
            if ret:
                arr = np.array(frame)
                arr = arr.reshape((1,img_size[0],img_size[1],1))
                arr = arr / 20
                p = GCF.predict(arr)
                p = p.reshape((p.shape[1],))
                
                if max(p) < 0.5:
                    pred = 7
                else:
                    pred = np.argmax(p)
                    
                print(f'current gesture: {pred} ; seq: {seq}')

                if pred == 8 and len(seq) == 0:
                    seq.append(pred)
                
                if len(seq) > 0:
                    if pred == seq[-1]:
                        continue
                    elif pred != 0 and pred != 7:
                        seq.append(pred)
                    elif pred == 0:
                        seq.append(pred)
                        decide_task(get_key(seq))
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
    