from screen_brightness_control import get_brightness, set_brightness
from pyautogui import press,screenshot,scroll,hotkey
from datetime import datetime

volume_up=lambda :press('volumeup')
volume_down=lambda :press('volumedown')

brightness_up=lambda :set_brightness(get_brightness()+10)
brightness_down=lambda :set_brightness(get_brightness()-10)

def take_screenshot():
    name=str(datetime.now())
    name=name.replace(' ','')
    name=name.replace(':','-')
    name=name.replace('.','')
    screenshot(f'{name}.png')

scroll_up= lambda : scroll(250)
scroll_down= lambda : scroll(-250)

press_enter= lambda :press('enter')
press_space=lambda :press('space')

def zoomin():
    hotkey('ctrl','+')

def zoomout():
    hotkey('ctrl','-')

def calendar():
    hotkey('win','alt','d') # firstcall opens and second call closes calender
    # very windows specific

def decide_task(arg:str):
    if arg=='c1':
      volume_up()
    elif arg=='c2':
      volume_down()
    elif arg=='c3':
      brightness_up()
    elif arg=='c4':
      brightness_down()
    elif arg=='c5':
      take_screenshot()
    elif arg=='c6':
      scroll_up()
    elif arg=='c7':
      scroll_down()
    elif arg=='c8':
      press_enter()
    elif arg=='c9':
      press_space()
    elif arg=='c10':
      zoomin()
    elif arg=='c11':
      zoomout()
    elif arg=='c12':
      calendar()
    else:
      print('No matching commands found!')