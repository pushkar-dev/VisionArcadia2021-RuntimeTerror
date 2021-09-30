# Vision Arcadia
## Team- Runtimeterror
## Members-
1. Vishesh Soni
2. Aditya Prakash
3. Ravneet Kaur
4. Pushkar Patel
5. Ayush Nigam

# Setting Up environment
1. Make sure you have latest (3.8+) python installation, and python and pip are added to path.
2. make a new folder and cd to that folder
   ```bash
   mkdir <dirname>
   cd <dirname>
   ```
3. Clone the repository in you local machine by executing
   ```bash
   git clone https://github.com/pushkar-dev/VisionArcadia2021-RuntimeTerror.git
   ```
4. Make a virtual environment
   ```bash
    virtualenv <name>
   ```
    you may need to install virtualenv first using pip.
5. Activate the environment
   ```bash
   <name>\Scripts\activate.ps1
   ```
   for cmd
   ```bash
   <name>\Scripts\activate
   ```
6. Install all the dependencies.
   ```bash
   pip install -r requirements.txt
   ```
   It may take a while.
9. Run the program 
   ```bash
   python interpreter.py
   ```
   now start showing gestures

# Instructions for Use
1. It will take a few seconds for camera to start, so that user gets ready.
2. Gesture list and gesture language are shown below.

# Gestures
There are 8 gestures<br>


# Gesture Language
1. c1 8,6,0 volume up
2. c2 8,5,0 volume down
3. c3 8,4,0 brightness up
4. c4 8,3,0 brightness down
5. c5 8,2,0 screenshot
6. c6 8,1,0 scroll up
7. c7 8,6,5,0 scroll down
8. c8 8,5,4,0 press enter
9. c9 8,4,3,0 press space
10. c10 8,3,2,0 zoomin
11. c11 8,2,1,0 zoomout
12. c12 8,1,6,0 open / close calender
