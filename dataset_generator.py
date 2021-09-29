import cv2,os,time
import warnings
warnings.filterwarnings('ignore')

def collect_gesture(size): # generates folder for a gesture inside main dataset

    folderName = f'datasets/{dataset_name}/{i}' # storage location
    if not os.path.exists(folderName):
        os.makedirs(folderName)
    
    cam = cv2.VideoCapture(0)
    img_counter = 0

    snap = 2   # shutter waiting time
    wait = 1   # count

    loop_num = size * snap
    for n in range(loop_num):
        
        if wait == snap: # captures image only when wait = snap
            
            ret, frame = cam.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame, (img_size,img_size), interpolation = cv2.INTER_AREA)
            
            if ret:
                cv2.imwrite(folderName+"/frame%d.jpg" %img_counter, frame)
                img_counter += 1
                print("Current File %d \r" %img_counter, end = '')
                cv2.imshow('frame', frame)
            else:
                break
            wait = 1
        else:
            wait += 1

    cam.release()
    cv2.destroyAllWindows()
    print("Created folder: " + folderName)

dataset_name = input('Enter dataset name : ')         # dataset name
img_size = int(input('Enter image dimension ^ 2 = ')) # image size
dataset_size = int(input('dataset_size : '))          # samples in one gesture

for i in ['s_','g1','g2','g3','g4','g5','g6','_s','na']: # makes dataset
    print()
    print(f'CAPTURING DATA : {i}')
    print()
    time.sleep(3) 
    collect_gesture(dataset_size)
    
